valores = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
pares = 0

if valores.count(9) > 0:
    print(f'O numero nove aparece {valores.count(9)} vez(es)')
else:
    print('O numero nove não aparece nenhuma vez')

if valores.count(3) > 0:
    print(f'O numero três apareceu na {valores.index(3) + 1} posição')
else:
    print('O numero três não aparece em nenhuma posição')

print('Numero(s) par(es) digitado(s): ', end='')
for x in range(0, len(valores)):
    if valores[x] % 2 == 0 and valores[x] != 0:
        print(valores[x], end=', ')
        pares += 1
if pares == 0:
    print('Nenhum!', end='')
