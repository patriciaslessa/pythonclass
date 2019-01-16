# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_9(a,b,c):
    """
    Faça um Programa que leia três números e mostre-os em ordem decrescente.
    >>> lista_2_ex_9(3,2,1)
    3,2,1
    >>> lista_2_ex_9(6,4,5)
    6,5,4
    >>> lista_2_ex_9(2,4,1)
    4,2,1
    >>> lista_2_ex_9(2,6,4)
    6,4,2
    >>> lista_2_ex_9(4,2,5)
    5,4,2
    >>> lista_2_ex_9(4,5,6)
    6,5,4
    """



    if (a > b) and (b > c):
        print(a,b,c)
    elif (a > b) and (c > b):
        print(a,c,b)
    elif (b > a) and (a > c):
        print(b,a,c)
    elif (b > a) and (c > a):
        print(b,c,a)
    elif (c > a) and (c > b) and (a > b):
        print(c,a,b)
    else:
        print(c,b,a)



test()

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

lista_2_ex_9(a,b,c)
