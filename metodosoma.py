"""
Documentação do metodo soma
"""

import builtins
import math



def soma(x, y):
    args_locals = locals()
    print(args_locals)

    return x + y

args_globals = globals()

print(args_globals['__name__'])
print(__name__)
