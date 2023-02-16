#!/bin/python3
'''
Copyright © 2023 Pyogenics <https://github.com/Pyogenics/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import sys
from shutil import rmtree
from marshal import load # I don't want to be importing extra stupid libs
from py_compile import compile
from dis import Bytecode, dis

from vm import VirtualMachine

def main():
    if len(sys.argv) < 2:
        print("Error: no file specified")
        sys.exit(64); # EX_USAGE

    # Compile all the supplied files into bytecode
    print("Compiling bytecode")
    for file in sys.argv[1::]:
        bytecode = compile(file, cfile=f"./tmp/{file}c") # XXX: Handle compile errors (doraise=True)
    print("Done")

    # Process bytecode and convert to brainfuck
    print("Processing bytecode")
    for file in sys.argv[1::]:
        file = f"tmp/{file}c" # Make the file be "./tmp/XXXXXXX.pyc"
        # I hate this so fucking much
        # Why can't dis just load the stupid file by itself
        # Why do I need to use extra stupid libraries to do it too
        with open(file, "rb") as raw:
            raw.read(16) # Skip past the header?
            file = load(raw)
        bytecode = Bytecode(file)
        VM = VirtualMachine(bytecode)
        VM.run()
        print(VM.stack)

    print("Done")
    
    print("Cleaning up")
    rmtree("./tmp")
    print("All done!")

if __name__ == "__main__":
    main()
