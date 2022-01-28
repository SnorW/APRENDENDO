matrix = [[],
          [],
          []
]

valor = []
for y in range(0, 3):
    for x in range(0, 3):
        valor_input = int(input(f'Digite um valor para posição [{y},{x}]: '))
        valor.append(valor_input)
        matrix[y].append(valor[:])
        valor.clear()
for x1, x2, x3 in matrix:
    print(x1, x2, x3)
