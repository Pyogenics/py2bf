# Python to brainfuck transpiler
This tool compiles python to bytecode and then transpiles the bytecode into brainfuck.

## Usage
```
./bf2py.py file1.py file2.py ...
```

## Compatibility
### Builtins
Only print is implemented

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
|STORE_NAME|no||
|DELETE_NAME|no||
|UNPACK_SEQUENCE|no||
|UNPACK_EX|no||
|STORE_ATTR|no||
