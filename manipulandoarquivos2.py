manipulando = open("arquivo.dat")

linha = manipulando.readline()

while linha:
    linha = linha.strip('\n')
    linha = linha.split('\t')
    print(linha)

    linha = manipulando.readline()


manipulando.close()

# for n, linha in enumerate(manipulando.readlines(), 1):
#     print(n, linha)
