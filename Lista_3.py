'''
8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

Ht = float(input('quanto você ganha por hora trabalhada, R$=',))
NHt = float(input('numero de horas trabalhada ao mês:'))
sal=Ht*NHt
#print('O salario do mês %0.2f' %sal)
print(f'O salario do mês {sal:20.2f}')
