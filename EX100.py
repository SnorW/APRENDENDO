from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando os valores')
    for x in range(0, 5):
        sleep(0.5)
        n_random = randint(1, 10)
        lst.append(n_random)
        print(n_random, end=' ')
    print()


def somaPares(lst):
    soma_pares = 0
    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma_pares += v
    print(f'A soma dos valores pares é: {soma_pares}')


lista = []
sorteio(lista)
somaPares(lista)
print(lista)