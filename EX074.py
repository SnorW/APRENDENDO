from random import randint
from math import inf
numeros_aleatorios = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior_valor = 0
menor_valor = inf

print('Os numeros sorteados foram: ')
for x in range(0, len(numeros_aleatorios)):
    print(f'{numeros_aleatorios[x]}', end='')
    print(', ' if x < len(numeros_aleatorios) - 1 else '', end='')

# Metodo que eu encontrei
    if numeros_aleatorios[x] > maior_valor:
        maior_valor = numeros_aleatorios[x]
    if numeros_aleatorios[x] < menor_valor:
        menor_valor = numeros_aleatorios[x]

# Metodo mais rapido / menos complicado / menor
# numeros_ordem = sorted(numeros_aleatorios)
# print(f'{numeros_ordem[0] é o menor valor e o {numeros_ordem[-1] é o maior valor}}')

# Metodo mais rapido ainda / menos complicado ainda / menor ainda
# print(f'\n{max(numeros)} é o maior valor')
# print(f'\n{min(numeros} é o menor valor')
print(f'\n{maior_valor} é o maior valor')
print(f'{menor_valor} é o menor valor')
