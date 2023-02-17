'''
Copyright © 2023 Pyogenics <https://github.com/Pyogenics/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from types import FunctionType, CodeType
from dis import Bytecode

# Local
from builtin import builtins

'''
This class does processing on the python bytecode

It will generate any additional bytecode (like from library functions) and
also pseudo simulate the execution of the bytecode so it can analyse it.
'''
class VirtualMachine:
    def __init__(self, bytecode):
        self.contexts = {}
        self.contextStack = []
        self.currentCtx = "global"

        # Create the global context
        self.contexts["global"] = context(bytecode)
        self.contexts["global"].co_names = builtins

    '''
    Public
    '''
    def run(self, ctx="global"):
        for instr in self.contexts[ctx].bytecode:
            match instr.opname:
                case "NOP":
                    self.i_nop(instr)
                case "LOAD_NAME":
                    self.i_load_name(instr)
                case "LOAD_GLOBAL":
                    self.i_load_global(instr)
                case "LOAD_CONST":
                    self.i_load_const(instr)
                case "CALL_FUNCTION":
                    self.i_call_function(instr)
                case "POP_TOP":
                    self.i_pop_top(instr)
                case "RETURN_VALUE":
                    self.i_return_value(instr)
                case "MAKE_FUNCTION":
                    self.i_make_function(instr)
                case "STORE_NAME":
                    self.i_store_name(instr)
                case other:
                    print(f"Unknown instruction '{instr.opname}'")

    def buildAll(self):
        return self.build("global")

    '''
    Private
    '''
    def build(self, ctx):
        program = ""
        for sub in self.contexts[ctx].program:
            program += sub
        return program

    def appendProg(self, sub):
        self.contexts[self.currentCtx].program.append(sub)

    def pushStack(self, item):
        self.contexts[self.currentCtx].stack.insert(0, item)

    def popStack(self, pos=0):
        return self.contexts[self.currentCtx].stack.pop(pos)

    def setStack(self, item, pos=0):
        self.contexts[self.currentCtx].stack[pos] = item

    def getStack(self, pos=0):
        return self.contexts[self.currentCtx].stack[pos]

    def newCtx(self, name, bytecode):
        self.contexts[name] = context(bytecode)
        self.contextStack.append(self.currentCtx)
        self.currentCtx = name

    def previousCtx(self):
        self.currentCtx = self.contextStack.pop()

    '''
    Instructions (https://docs.python.org/3/library/dis.html#python-bytecode-instructions)
    '''
    def i_nop(self, instr):
        pass #self.contexts[self.currentCtx].program += ""

    def i_load_name(self, instr):
        self.pushStack(self.contexts[self.currentCtx].co_names[instr.argval])

    def i_load_global(self, instr):
        self.pushStack(self.contexts["global"].co_names[instr.argval])

    def i_load_const(self, instr):
        self.pushStack(instr.argval)
        if type(instr.argval) is str:
            program = ""
            for char in instr.argval:
                program += ">" # The first byte is skipped, a NULL byte to mark the start
                program += ord(char) * "+"
            program += ">>" # Leave an extra byte, a NULL byte to mark the end
            self.appendProg(program)

    def i_call_function(self, instr):
        self.appendProg(self.getStack(instr.arg))

    def i_pop_top(self, instr):
        self.popStack()

        #XXX: Delete the item on the brainfuck stack too

    def i_return_value(self, instr):
        #XXX: Implement this when we do more stuff with functions
        pass

    def i_make_function(self, instr):
        # Convert function to brainfuck and push into co_names
        name = self.getStack(0)
        func = Bytecode(self.getStack(1))

        self.newCtx(name, func)
        self.run(name) # Recursion, whooo!
        program = self.build(name)

        self.previousCtx()
        self.setStack(program, 1)

    def i_store_name(self, instr):
        name = self.popStack()
        program = self.popStack()
        self.contexts[self.currentCtx].program.pop(-1) # Remove the name from brainfuck stack
        self.contexts[self.currentCtx].co_names[name] = program

'''
Helper class to store the current VM context
'''
class context:
    def __init__(self, bytecode):
        self.co_names = {}
        self.stack = []
        self.bytecode = bytecode
        self.program = [] # Brainfuck program
