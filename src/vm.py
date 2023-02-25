'''
Copyright © 2023 Pyogenics <https://github.com/Pyogenics/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from types import CodeType, NoneType
from dis import Bytecode

# Local
from vmBuiltins import bfBuiltins

'''
This class does processing on the python bytecode

It will generate any additional bytecode (like from library functions) and
also pseudo simulate the execution of the bytecode so it can analyse it.
'''
class VirtualMachine:
    contexts = {}
    contextStack = []
    currentContext = "global"

    def __init__(self, bytecode):
        self.contexts["global"] = Context(bytecode)
        self.contexts["global"].co_objects = bfBuiltins

    def runContext(self, ctx="global"):
        for instr in self.contexts[ctx].bytecode:
            match instr.opname:
                case "NOP":
                    self.i_NOP(instr)
                case "POP_TOP":
                    self.i_POP_TOP(instr)
                case "STORE_NAME":
                    self.i_STORE_NAME(instr)
                case "LOAD_CONST":
                    self.i_LOAD_CONST(instr)
                case "LOAD_NAME":
                    self.i_LOAD_NAME(instr)
                case "LOAD_GLOBAL":
                    self.i_LOAD_GLOBAL(instr)
                case "LOAD_FAST":
                    self.i_LOAD_FAST(instr)
                case "RETURN_VALUE":
                    self.i_RETURN_VALUE(instr)
                case "CALL_FUNCTION":
                    self.i_CALL_FUNCTION(instr)
                case "MAKE_FUNCTION":
                    self.i_MAKE_FUNCTION(instr)
                case other:
                    print(f"Unknown instruction {instr.opname}")

    def buildProgram(self):
        return self.contexts["global"].buildProgram()

    def injectArgs(self, function, args):
        chunks = function.split("#")

        for chunkIdx, chunk in enumerate(chunks):
            if chunk[:3] == "arg":
                argNum = int(chunk[3:])
                chunks[chunkIdx] = self.encodeStr(args[argNum])

        newFunc = ""
        for sub in chunks:
            newFunc += sub
        return newFunc

    def useNewContext(self, name, bytecode):
        self.contexts[name] = Context(bytecode)
        self.contextStack.append(self.currentContext)
        self.currentContext = name

    def usePreviousContext(self):
        self.currentContext = self.contextStack.pop()

    def encodeStr(self, string):
        bfString = ""
        for char in string:
            bfString += ">"
            bfString += "+" * ord(char)
        bfString += ">>" # Null terminated
        return bfString

    '''
    Instructions
    '''
    def i_NOP(self, instr):
        pass

    def i_POP_TOP(self, instr):
        self.contexts[self.currentContext].pop()

    def i_STORE_NAME(self, instr):
        # Assuming that this consumes the stack
        obj = self.contexts[self.currentContext].pop()
        self.contexts[self.currentContext].co_objects[instr.argval] = obj

    def i_LOAD_CONST(self, instr):
        self.contexts[self.currentContext].push(instr.argval)

        # Push to BF stack
        bfEncodedData = ""
        match instr.argval:
            case str():
                bfEncodedData = self.encodeStr(instr.argval)
            case CodeType():
                pass
            case NoneType():
                pass
            case other:
                print(f"unknown data type {type(instr.argval)}")

        self.contexts[self.currentContext].appendSubProgram(bfEncodedData)
                
    def i_LOAD_NAME(self, instr):
        obj = self.contexts[self.currentContext].co_objects[instr.argval]
        self.contexts[self.currentContext].push(obj)

    # XXX: This should be the same as LOAD_CONST!
    # It would cause problems with type conversion,
    # perhaps custom objects for BF encoded data?
    def i_LOAD_GLOBAL(self, instr):
        obj = self.contexts["global"].co_objects[instr.argval]
        self.contexts[self.currentContext].push(obj)

    def i_LOAD_FAST(self, instr):
        obj = f"#arg{instr.arg}#" # The actual values are injected by CALL_FUNCTION
        self.contexts[self.currentContext].appendSubProgram(obj)
        self.contexts[self.currentContext].push(obj)

    # How would this work?
    def i_RETURN_VALUE(self, instr):
        self.i_NOP(instr)

    # XXX: Maybe arguments should be baked into the function at transpile time?
    # The bytecode to BF transpile would need to happen here instead and MAKE_FUNCTION just pop the name?
    # Perhaps leave MAKE_FUNCTION alone and inject the variables here? E.g. make a copy here and build that with the
    # injected variables (args).
    def i_CALL_FUNCTION(self, instr):
        args = []
        for idx in range(instr.arg):
            args.append(self.contexts[self.currentContext].pop())
        args.reverse()
        func = self.contexts[self.currentContext].pop()

        func = self.injectArgs(func, args)
        self.contexts[self.currentContext].appendSubProgram(func)
        self.contexts[self.currentContext].push(None) # Use None as a place holder for the return value on the simulated stack, we can't really simulate return values?

    def i_MAKE_FUNCTION(self, instr):
        name = self.contexts[self.currentContext].pop()
        bytecode = self.contexts[self.currentContext].pop()

        self.useNewContext(name, bytecode)
        self.runContext(name)
        self.usePreviousContext()
        self.contexts[self.currentContext].push(self.contexts[name].buildProgram())
        self.contexts[self.currentContext].removeSubProgram(-1) # Remove object name from bf program

        # The function context is no longer needed
        del self.contexts[name]

'''
Helper class to store program context information
'''
class Context:
    def __init__(self, bytecode):
        self.bytecode = Bytecode(bytecode)
        self.program = []
        self.stack = []
        self.co_objects = {} # Dictionary to store co_names and their objects

    def buildProgram(self):
        program = ""
        for sub in self.program:
            program += sub
        return program

    def appendSubProgram(self, sub):
        self.program.append(sub)

    def removeSubProgram(self, idx):
        del self.program[idx]

    def push(self, item, pos=0):
        self.stack.insert(pos, item)

    def pop(self, pos=0):
        return self.stack.pop(pos)

    def set(self, item, pos=0):
        self.stack[pos] = item

    def get(self, pos=0):
        return self.stack[pos]
