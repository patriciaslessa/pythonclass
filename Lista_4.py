##'''
##9 Faça um Programa que peça a temperatura em graus Farenheit,
##transforme e mostre a temperatura em graus Celsius.
##C = (5 * (F-32) / 9).

##'''

F = float(input("qual a temperatura em Farenheit?"))
C = (5*(F-32)/9)
print('A temperatura %0.2f' %C)

print(f"A temperatura {5*(F-32)/9}")
