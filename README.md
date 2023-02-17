# Python to brainfuck transpiler
This tool compiles python to bytecode and then transpiles the bytecode into brainfuck.

## Usage
Tested on python 3.10
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
py2bf only supports python 3.7 and newer, for now.
Information relative to python 3.11.2:
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
|DELETE_ATTR|no||
|STORE_GLOBAL|no||
|DELETE_GLOBAL|no||
|LOAD_CONST|yes||
|LOAD_NAME|yes||
|BUILD_TUPLE|no||
|BUILD_LIST|no||
|BUILD_SET|no||
|BUILD_MAP|no||
|BUILD_CONST_KEY_MAP|no||
|BUILD_STRING|no||
|LIST_TO_TUPLE|no||
|LIST_EXTEND|no||
|SET_UPDATE|no||
|DICT_UPDATE|no||
|DICT_MERGE|no||
|LOAD_ATTR|no||
|COMPARE_OP|no||
|IS_OP|no||
|CONTAINS_OP|no||
|IMPORT_NAME|no||
|IMPORT_FROM|no||
|JUMP_FORWARD|no||
|JUMP_BACKWARD|no||
|JUMP_BACKWARD_NO_INTERRUPT|no||
|POP_JUMP_FORWARD_IF_TRUE|no||
|POP_JUMP_BACKWARD_IF_TRUE|no||
|POP_JUMP_FORWARD_IF_FALSE|no||
|POP_JUMP_BACKWARD_IF_FALSE|no||
|POP_JUMP_FORWARD_IF_NOT_NONE|no||
|POP_JUMP_BACKWARD_IF_NOT_NONE|no||
|POP_JUMP_FORWARD_IF_NONE|no||
|POP_JUMP_BACKWARD_IF_NONE|no||
|JUMP_IF_TRUE_OR_POP|no||
|JUMP_IF_FALSE_OR_POP|no||
|FOR_ITER|no||
|LOAD_GLOBAL|yes||
|LOAD_FAST|no||
|STORE_FAST|no||
|DELETE_FAST|no||
|MAKE_CELL|no||
|LOAD_CLOSURE|no||
|LOAD_DEREF|no||
|LOAD_CLASS_DEREF|no||
|STORE_DEREF|no||
|DELETE_DEREF|no||
|COPY_FREE_VARS|no||
|RAISE_VARARGS|no||
|CALL|no||
|CALL_FUNCTION_EX|no|CALL_FUNCTION is implemented|
|LOAD_METHOD|no||
|PRECALL|no||
|PUSH_NULL|no||
|KW_NAMES|no||
|MAKE_FUNCTION|yes|Flags not implemented|
|BUILD_SLICE|no||
|EXTENDED_ARG|no||
|FORMAT_VALUE|no||
|MATCH_CLASS|no||
|RESUME|no||
|RETURN_GENERATOR|no||
|SEND|no||
|ASYNC_GEN_WRAP|no||
|HAVE_ARGUMENT|no||
