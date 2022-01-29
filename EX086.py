matrix = [
]

valor = []
for y in range(0, 3):
    for x in range(0, 3):
        valor_input = int(input(f'Digite um valor para posição [{y},{x}]: '))
        valor.append(valor_input)
    matrix.append(valor[:])
    valor.clear()

for y in range(0, 3):
    for x in range(0, 3):
        print(f'[{matrix[y][x]:^5}]', end='')
    print()