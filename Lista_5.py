##Faça um Programa que peça a temperatura em graus Celsius,
##transforme e mostre em graus Farenheit.

C = float(input("Qual a temperatura em Celsius?"))
F = (9*C/5+32)
#print("A temperatura %0.2f" %F)
print(f"A temperatura {9*C/5 + 32}")
