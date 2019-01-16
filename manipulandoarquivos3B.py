# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#

with open("a.txt", "w") as arq:
    arq.write("200.135.80.9, 192.168.1.1, 8.35.67.74, 257.32.4.5, 85.345.1.2, 1.2.3.4, 9.8.234.5, 192.168.0.256")

with open("a.txt") as arq:
    ler = arq.read()
    lista_ip = ler.split(",")

    for ip in lista_ip:
        q = open("b.txt", "a")
        q.write(ip)

        list_n_ip = ip.split(".")
        if int(list_n_ip[0]) % 2 == 0:
            p = open("par.txt", "a")
            p.write(ip+'\n')
            p.close()
        else:
            p = open("impar.txt", "a")
            p.write(ip+'\n')
            p.close()

        print(ip+'\n')

        q.close()
