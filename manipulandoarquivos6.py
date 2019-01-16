import glob

l = list (range(0,10))
str_p = "file_"
#print(glob.glob("*"))
print(glob.glob(f'{str_p}*'))

l_arq = glob.glob(f'{str_p}*')

num_min = 2
file_min = ''
num_max = 0
file_max = ''

for arq in l_arq:
    print(arq)
    q = open(arq)
    ler = q.read()
    #print(ler)
    q.close()

    lista_arq = ler.split("\n")
    #print(lista_arq)

    for l in lista_arq:
        l = l.strip("\n")
        #print(l)
        if l:
            num = float(l)
            print(num)
            if num < num_min:
                num_min = num
                file_min = arq

            if num > num_max:
                num_max = num
                file_max = arq

min = open('min.txt', 'w')
min.write(f'{file_min}\t{num_min}')
min.close()

max = open('max.txt', 'w')
max.write(f'{file_max}\t{num_max}')
max.close()
