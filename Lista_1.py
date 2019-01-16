'''wiki python
listas
'''

x = [5,2,3,10]

n =len(x)

sum = 0
for _x in x:
    sum = sum + _x
print(sum)
mean = sum/n
print(mean)

'''
5 Faça um Programa que converta metros para centímetros.

'''

D = 3
conv = D*100
print(conv)

'''
6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''

import math

valor_r = float(input('Digite o raio'))
area = valor_r*math.pi**2
print('O valor', area)
