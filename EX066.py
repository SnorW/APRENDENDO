num = 0
soma = 0
cont_num = 0

while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    cont_num += 1
    soma += num
print(f'A Soma de {cont_num} valores digitados é igual a {soma}')
