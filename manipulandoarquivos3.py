# 1 Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.O arquivo de entrada possui o seguinte formato:
#

with open("a.txt", "w") as arq:
    arq.write("200.135.80.9, 192.168.1.1, 8.35.67.74, 257.32.4.5, 85.345.1.2, 1.2.3.4, 9.8.234.5, 192.168.0.256")

with open("a.txt") as arq:
    print (arq.read())
