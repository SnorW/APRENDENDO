n2 = 0
n3 = 0
pares = 0
impares = 0
for x in range(0, 6):
    n1 = int(input('Digite um numero'))
    if n1 % 2 != 1:
        n2 += n1
        pares += 1
    elif n1 % 2 == 1:
        n3 += n1
        impares += 1
print('A soma desses {} pares é {}'.format(pares, n2))
print('A soma desses {} impares é {}'.format(impares, n3))
