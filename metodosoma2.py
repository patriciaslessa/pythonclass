"""
Documentação do metodo soma
"""


def soma(x, y):
    args_locals = locals()
    print(args_locals)

    return x + y

args_globals = globals()

if __name__ == '__main__':
    resulta = soma(2, 3)
    print(resulta)
