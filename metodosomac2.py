"""
Documentação do metodo soma
"""


def soma(x, y):
    """
    soma(x, y) -> result
    """

    res = x + y
    args_locals = locals()
#    print(args_locals)
    return res

args_globals = globals()

if __name__ == '__main__':
    resulta = soma(2, 3)
    print(resulta)
    resulta = soma(2, 3, 4)
    print(resulta)
