a = float(input('Digite o valor de um dos arestas'))
b = float(input('Digite o segundo valor de um dos arestas'))
c = float(input('Digite o terceiro valor de um dos arestas'))

condicaotriangulo = a - b < c < a + b
condicaoequilatero = a == b == c
condicaoisoceles = a == b != c or b == c != a or a == c != b
condicaoescaleno = a != b != c != a

if condicaotriangulo:
    print('Seu triangulo é possível')
    if condicaoequilatero:
        print('Seu triangulo é equilátero')
    elif condicaoisoceles:
        print('Seu triangulo é isóceles')
    elif condicaoescaleno:
        print('Seu triangulo é escaleno')
else:
    print('Seu triangulo não é possível')
