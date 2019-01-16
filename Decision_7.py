# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_7(a,b,c):
    """
     Faça um Programa que leia três números e mostre o maior e o menor deles.
    >>> lista_2_ex_7(1,2,3)
    3,1
    >>> lista_2_ex_7(1,4,2)
    4,1
    >>> lista_2_ex_7(5,3,1)
    5,1
    """

    # a = input()
    # b = input()
    # c = input()



    if float(a) > float(b) and float(a) > float(c):
        max = (a)
    elif float(c) > float(a) and float(c) > float(b):
        max = (c)
    else:
        max = (b)

    if float(b) < float(a) and float(b) < float(c) and float(a) < float(c):
        min = (b)
    elif float(c) < float(a) and float(c) < float(b) and float(b) < float(a):
        min = (c)
    else:
        min = (a)

    print(str(max)+','+str(min))
test()

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

lista_2_ex_7(a,b,c)
