# coding: UTF-8

def test():
    import doctest
    doctest.testmod(verbose=True)

def lista_2_ex_5(a,b):
    """
     Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    >>> lista_2_ex_5(5.0,9.0) #A mensagem "Reprovado", se a média for menor do que sete;
    Aprovado
    >>> lista_2_ex_5(4.0,8.0) #A mensagem "Aprovado com Distinção", se a média for igual a dez;
    Reprovado
    >>> lista_2_ex_5(10.0,10.0)
    Aprovado com Distinção
    """



    if float((a+b)/2) == 10.0:
        print('Aprovado com Distinção')
    elif float((a+b)/2) >= 7.0:
        print ('Aprovado' )
    else:
        print('Reprovado')


a = float(input('a: '))
b = float(input('b: '))

lista_2_ex_5(a,b)
test()

#print(lista_2_ex_5)
#print(help(lista_2_ex_5))
