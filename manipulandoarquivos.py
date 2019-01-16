manipulando = open("arquivo.dat")

leitura = manipulando.readlines()
n = len(leitura)
total_age = 0
min_idade = 10**3
max_idade = 0
nome_min_id = ""
nome_max_id = ""

for linha in leitura:
    linha = linha.strip('\n')
    linha = linha.split('\t')

    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])

    if idade < min_idade:
        min_idade = idade
        nome_min_id = nome

    if idade > max_idade:
        max_idade = idade
        nome_max_id = nome

    total_age = total_age + idade

    print(f"id: {id}; nome: {nome}; idade: {idade}")

media = (total_age/n)


print(f"Soma das idades: {total_age}")
print(f"Media de idades: {media}")
print (f"O mais novo e: {min_idade} e seu nome e: {nome_min_id}")
print (f"O mais velho e: {max_idade} e seu nome e: {nome_max_id}")

ssq= 0

for linha in leitura:
    linha = linha.strip('\n')
    linha = linha.split('\t')

    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])

    ssq = ssq + (idade - media)**2

std = (ssq/(n-1))**(1/2)

print(f"Desvio Padrao de idades: {std}")

manipulando.close()
