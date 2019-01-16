"""
Usar o modulo soma
"""

def soma(*args):
    """
    soma(x, y, z,...) -> result
    """

    return sum(args)


if __name__ == '__main__':
    resulta = soma(1, 2, 3, 4, 5, 6)
    print(resulta)
    l = [1, 2, 3, 4]
    print(soma(*l))
