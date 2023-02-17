# Python to brainfuck transpiler
This tool compiles python to bytecode and then transpiles the bytecode into brainfuck.

## Usage
```
./bf2py.py file1.py file2.py ...
```
## Working example
This is about the most functionality you can get out of this so far.
```python
print("This is an example program")

def myFunction():
    print("Basic functions work!")

myFunction()
```

## Compatibility
Relative to python 3.11.2
### Builtins
Only print is implemented

### Builtin types
|Name|Status|Note|
|----|------|----|
|int|no||
|float|no||
|complex|no||
|list|no||
|tuple|no||
|range|no||
|str|yes||
|bytes|no||
|bytearray|no||
|memoryview|no||
|set|no||
|frozenset|no||
|dict|no||
|generic|no||
|alias|no||
|union|no||

### Instructions
|Name|Status|Note|
|----|------|----|
|NOP |yes   |    |
|POP_TOP|yes|    |
|COPY|no||
|SWAP|no||
|CACHE|no||
|UNARY_POSITIVE|no||
|UNARY_NEGATIVE|no||
|UNARY_NOT|no||
|UNARY_INVERT|no||
|GET_ITER|no||
|GET_YIELD_FROM_ITER|no||
|BINARY_OP|no||
|BINARY_SUBSCR|no||
|STORE_SUBSCR|no||
|DELETE_SUBSCR|no||
|GET_AWAITABLE|no||
|GET_AITER|no||
|GET_ANEXT|no||
|END_ASYNC_FOR|no||
|BEFORE_ASYNC_WITH|no||
|PRINT_EXPR|no||
|SET_ADD|no||
|LIST_APPEND|no||
|MAP_ADD|no||
|RETURN_VALUE|no|Added but not implemented yet|
|YIELD_VALUE|no||
|SETUP_ANNOTATIONS|no||
|IMPORT_STAR|no||
|POP_EXCEPT|no||
|RERAISE|no||
|PUSH_EXC_INFO|no||
|CHECK_EXC_MATCH|no||
|CHECK_EG_MATCH|no||
|PREP_RERAISE_STAR|no||
|WITH_EXCEPT_START|no||
|LOAD_ASSERTION_ERROR|no||
|LOAD_BUILD_CLASS|no||
|BEFORE_WITH|no||
|GET_LEN|no||
|MATCH_MAPPING|no||
|MATCH_SEQUENCE|no||
|MATCH_KEYS|no||
|STORE_NAME|yes||
|DELETE_NAME|no||
|UNPACK_SEQUENCE|no||
|UNPACK_EX|no||
|STORE_ATTR|no||
