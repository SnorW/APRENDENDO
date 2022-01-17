n1 = int(input('Digite um numero: '))

for x in range(2, n1 + 1):
    if x != n1 and n1 % x == 0 or n1 == 1:
        print('{} não é um numero primo'.format(n1))
        break
    elif x == n1 and n1 % x == 0:
        print('{} é um numero primo!'.format(n1))
        break
