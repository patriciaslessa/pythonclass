"""
Documentação
"""

import builtins

print(dir(builtins))

def soma(x, y):
    args_locals = locals()
    print(args_locals)

    return x + y

args_globals = globals()
print(args_globals)
