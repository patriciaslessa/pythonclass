
#def lista_2_ex_1():
"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

i = 0
number = input("Digite um numero: ")
number = int(number)
print(f"Tabuada de {number}: ")

while (i < 10):
    i = i + 1
    tabuada = (i*number)
    show = f"{number} X {i} = {tabuada}"
    print(show)
