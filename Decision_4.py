# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_4(letra):
    """
     Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
     >>> lista_2_ex_4('a')
     vogal
     >>> lista_2_ex_4('m')
     consoante
    """

    vogais = ['a','e','i','o','u']

    if letra in vogais:
        print ("vogal" )
    else:
        print ("consoante")

let = input("Digite uma letra:")
lista_2_ex_4(let)
test()

print(lista_2_ex_4)
print(help(lista_2_ex_4))
