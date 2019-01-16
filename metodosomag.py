"""
Usar o modulo soma
"""

def soma(*args, **kwargs):
    """
    soma(x, y, z,...) -> result
    """

    # import pdb; pdb.set_trace() # forma tradicional
    # breakpoint() #nova em pyton 3.7

    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
    l = [1,1]
    d = {'x': 2, 'x1': 2, 'x2': 2}

    print(soma(*l, **d))
#    print(soma(e=2, *l, **d))
