from random import sample
import time
numeros_sorteados = []
jogos = int(input('Quantos jogos você quer gerar?'))

print('-='*15, f'Sorteando {jogos} jogos', '-='*15)

for x in range(0, jogos):
    jogos_random = sample(range(1, 60), 6)
    jogos_random.sort()
    numeros_sorteados.append(jogos_random[:])

for seq in numeros_sorteados:
    time.sleep(0.3)
    print(f'Jogo {numeros_sorteados.index(seq)+1}: {seq:>5}')
print('-='*35)
