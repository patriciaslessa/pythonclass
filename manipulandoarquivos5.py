import glob

l = list (range(0,10))
str_p = "file_"
#print(glob.glob("*"))
print(glob.glob(f'{str_p}*'))

l_arq = glob.glob(f'{str_p}*')

for arq in l_arq:
    print(arq)
    q = open(arq)
    print(q.read())
    q.close() 
