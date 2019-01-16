# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_6(a,b,c):
    """
     Faça um Programa que leia três números e mostre o maior deles.
    >>> lista_2_ex_6(1, 2, 3)
    3
    >>> lista_2_ex_6(1, 4, 2)
    4
    >>> lista_2_ex_6(5, 3, 1)
    5
    """

    # a = input()
    # b = input()
    # c = input()



    if a > c and a > b:
        print (a)
    elif b > c and b > a:
        print (b)
    else:
        print (c)



test()

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

lista_2_ex_6(a,b,c)
