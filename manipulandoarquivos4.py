import random

l = list (range(0,10))
str_p = "file_"

for _ in l:
    num = random.choice(l)
    r = open(f"{str_p}{num}.txt","a")
    r.write(f'{random.random()}\n')
    r.close()
