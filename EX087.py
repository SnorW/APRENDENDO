matrix = [
]

valor = []
soma_pares = 0
soma_terceiracoluna = 0
maior_segundalinha = 0

for y in range(0, 3):
    for x in range(0, 3):
        valor_input = int(input(f'Digite um valor para posição [{y},{x}]: '))
        valor.append(valor_input)
        if valor_input % 2 == 0:
            soma_pares += valor_input
        if x == 2:
            soma_terceiracoluna += valor_input
        if y == 1:
            if valor_input > maior_segundalinha:
                maior_segundalinha = valor_input
    matrix.append(valor[:])
    valor.clear()

for y in range(0, 3):
    for x in range(0, 3):
        print(f'[{matrix[y][x]:^5}]', end='')
    print()

print('=-'*40)
print(f'O maior valor da segunda linha é {maior_segundalinha}.')
print(f'A soma dos valores da terceira coluna é {soma_terceiracoluna}.')
print(f'A soma dos valores pares é {soma_pares}.')
