
"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.

"""
fib_0 = 0
fib_1 = 1
fib_2 = fib_0 + fib_1
print(fib_0)
print(fib_1)
print(fib_2)

for i in range(20):
    fib_3 = fib_2 + fib_1
    fib_1 = fib_2
    fib_2 = fib_3

    print(fib_3)
