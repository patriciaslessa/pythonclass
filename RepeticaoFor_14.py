
#def lista_2_ex_1():
"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.

"""

n_par = 0
n_impar = 0

for i in range(1,11):
    number = input("Digite um numero: ")
    n = int(number)
    print(f" {n}")

    if (n % 2 == 0 ):
        n_par = n_par + 1
    else:
        n_impar = n_impar + 1

print (f"n_par: {n_par} e n_impar: {n_impar}")
