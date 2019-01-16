
"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.

"""
# append = fib += [fib[i - 1] + fib[i - 2]]

N = int(input ("Digite a quantidade da serie de fib: "))
fib = [0,1,1]

for i in range(3,N):
    fib.append(fib[i-1] + fib[i-2])

for seq in fib:
    print(seq)
