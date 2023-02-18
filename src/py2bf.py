#!/bin/python3
'''
Copyright © 2023 Pyogenics <https://github.com/Pyogenics/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import sys
from marshal import load
from py_compile import compile

from vm import VirtualMachine

def compileBytecode(files):
    bytecodePaths = []
    for file in files:
        bytecodePaths.append(compile(file, cfile=f"bytecode/{file}"))
    return bytecodePaths

def transpileBytecode(filePaths):
    bfPrograms = []
    for file in filePaths:
        with open(file, "rb") as pyc:
            pyc.read(16) # Skip header (python < 3.7 uses a 12 byte header)
            VM = VirtualMachine(load(pyc))
            VM.runContext()
            bfPrograms.append(VM.buildProgram())
    return bfPrograms

def main():
    if len(sys.argv) < 2:
        print("Error: no file specified")
        sys.exit(64); # EX_USAGE

    # Compile all the supplied files into bytecode
    print("Compiling bytecode.....", end=" ")
    bytecodePaths = compileBytecode(sys.argv[1::])
    print("Done")
    
    # Process bytecode and convert to brainfuck
    print("Processing bytecode.....", end=" ")
    bfPrograms = transpileBytecode(bytecodePaths)
    print("Done")

    for name, file in zip(sys.argv[1::], bfPrograms):
        print(f"{name}:\n{file}")

if __name__ == "__main__":
    main()
