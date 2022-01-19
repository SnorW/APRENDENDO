# Código menos intuitivo, veja o EX061
num = int(input('Digite um valor: '))
num_variavel = num
f = 1

for x in range(1, num):
    f *= num_variavel
    num_variavel -= 1

print('O fatorial de {} é igual a {}'.format(num, f))
