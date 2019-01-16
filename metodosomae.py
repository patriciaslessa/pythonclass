"""
Usar o modulo soma
"""

import metodosomac as func
from metodosomac import soma

if __name__ == '__main__':
    res = func.soma(4,5)
    print(res)
    res = soma(3,4)
    print(res)
    print(help(func))
