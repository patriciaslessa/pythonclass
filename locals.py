"""
Documentação
"""

print(__doc__)
print(__file__)

def soma(x, y):
    args_locals = locals()
    print(args_locals)

    return x + y

args_globals = globals()
print(args_globals)
