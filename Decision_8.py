# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_8(a,b,c):
    """
    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
    >>> lista_2_ex_8(1.00,2.00,3.00)
    1.00
    >>> lista_2_ex_8(6.00,4.00,2.00)
    2.00
    >>> lista_2_ex_8(5.00,3.00,4.00)
    3.00
    """

    # a = input()
    # b = input()
    # c = input()




    if float(b) < float(a) and float(b) < float(c):
        price = (b)
    elif float(c) < float(a) and float(c) < float(b):
        price = (c)
    else:
        price = (a)

    print(f"{price:0.2f}")
test()

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

lista_2_ex_8(a,b,c)
