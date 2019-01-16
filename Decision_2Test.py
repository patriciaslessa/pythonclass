
def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_2(valor):
    """
     Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
     >>> lista_2_ex_2(1)
     positivo
     >>>lista_2_ex_2(-2.5)
     negativo
     >>>lista_2_ex_2(0)
     positivo
    """
#    a = int(input("digite um número: "))

    if float(valor) >= 0:
        print ("positivo" )
    else:
        print ("negativo")

val = input("Digite um valor:")
lista_2_ex_2(val)
