from random import randint
from operator import itemgetter

jogadas_temp = {}

jogadorn1 = randint(1, 6)
jogadorn2 = randint(1, 6)
jogadorn3 = randint(1, 6)
jogadorn4 = randint(1, 6)

jogadas_temp['Jogador N°1'] = jogadorn1
jogadas_temp['Jogador N°2'] = jogadorn2
jogadas_temp['Jogador N°3'] = jogadorn3
jogadas_temp['Jogador N°4'] = jogadorn4

cont = 1

for k, v in jogadas_temp.items():
    print(f'{k}: {v}')

jogadas_sorted = sorted(jogadas_temp.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(jogadas_sorted):
    print(f'O {i+1}° lugar é o {v[0]} que tirou {v[1]}')
