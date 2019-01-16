nome_arq = "arquivo.dat"
arq_add = open(nome_arq, "a")
arq_add.write("6\tet\t22\n")
arq_add.close ()


ler = open(nome_arq)
leitura = ler.read()

print(leitura)
print(leitura)
ler.close()
