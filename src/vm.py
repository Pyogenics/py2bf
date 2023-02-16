'''
Copyright © 2023 Pyogenics <https://github.com/Pyogenics/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from dis import dis

# Local
from builtin import builtins

'''
This class does processing on the python bytecode

It will generate any additional bytecode (like from library functions) and
also pseudo simulate the execution of the bytecode so it can analyse it.
'''
class VirtualMachine:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.stack = []
        self.contexts = {}
        self.currentCtx = "global"

        # Create the global context
        self.contexts["global"] = context()
        self.contexts["global"].co_names = builtins;

    def run(self):
        for instr in self.bytecode:
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
                case other:
                    print("Unknown instruction")

    def build(self):
        return self.contexts["global"].program

    def appendProg(self, sub):
        self.contexts[self.currentCtx].program += sub

    '''
    Instructions
    '''
    def i_nop(self, instr):
        pass #self.contexts[self.currentCtx].program += ""

    def i_load_name(self, instr):
        self.stack.insert(0, instr.argval)

    def i_load_global(self, instr):
        self.i_load_name(instr)

    def i_load_const(self, instr):
        self.stack.insert(0, instr.argval)
        #XXX: Implement type based copying!!!!! We can only do strings
        if instr.argval == None:
            return 0;

        for char in instr.argval:
            self.appendProg(ord(char) * "+")
            self.appendProg(">")
        
        self.appendProg("<" * len(instr.argval))

    def i_call_function(self, instr):
        self.appendProg(self.contexts[self.currentCtx].co_names[self.stack[instr.arg]])

    def i_pop_top(self, instr):
        del self.stack[0]

        #XXX: Delete the item on the brainfuck stack too

    def i_return_value(self, instr):
        #XXX: Implement this when we do more stuff with functions
        pass

'''
Helper class to store the current VM context
'''
class context:
    def __init__(self):
        self.co_names = {}
        self.co_consts = {}
        self.program = "" # Brainfuck program
