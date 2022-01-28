matrix = [[],
          [],
          []]

valor = []
soma_pares = 0
soma_terceiracoluna = 0
maior_segundalinha = 0

for y in range(0, 3):
    for x in range(0, 3):
        valor_input = int(input(f'Digite um valor para posição [{y},{x}]: '))
        valor.append(valor_input)
        matrix[y].append(valor[:])
        if valor_input % 2 == 0:
            soma_pares += valor_input
        if x == 2:
            soma_terceiracoluna += valor_input
        if y == 1:
            if valor_input > maior_segundalinha:
                maior_segundalinha = valor_input
        valor.clear()

for x1, x2, x3 in matrix:
    print(x1, x2, x3)

print('=-'*60)
print(f'O maior valor da segunda linha é {maior_segundalinha}')
print(f'A soma dos valores da terceira coluna é {soma_terceiracoluna}')
print(f'A soma dos valores pares é {soma_pares}')
