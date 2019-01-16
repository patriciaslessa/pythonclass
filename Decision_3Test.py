def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_3(sexo):
    """
     Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
     >>> lista_2_ex_3('F')
     Feminino
     >>> lista_2_ex_3('M')
     Masculino
     >>> lista_2_ex_3('G')
     Sexo Inválido
    """

#    l = int(input("digite F - Feminino ou M - Masculino: "))

    if not (sexo in ['F', 'f','m','M']):
        print ("Sexo Inválido")
    elif (sexo in ['F', 'f']):
        print ("Feminino" )
    else:
        print ("Masculino")
sex = input("Digite F ou M de acordo com o Sexo:")
lista_2_ex_3(sex)
test()

print(lista_2_ex_3)
print(help(lista_2_ex_3))
