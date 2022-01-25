lista = []
posicao_maior = []
index_maior = 0
index_menor = 0

for x in range(1, 6):
    valor = int(input(f'Digite um valor para a {x}ª posição: '))
    lista.append(valor)

print(f'\nOs valores digitados foram {lista}')
print(f'{max(lista)} é o maior valor digitado e ele aparece na(s) ', end='')
for x in range(0, lista.count(max(lista))):
    print(f'{lista.index(max(lista), index_maior) + 1}', end='ª')
    print(', ' if x + 1 < lista.count(max(lista)) else '', end='')
    index_maior = lista.index(max(lista), index_maior) + 1

if lista.count(max(lista)) == 1:
    print(' posição', end='')
else:
    print(' posições', end='')

print(f'\n{min(lista)} é o menor valor digitado e aparece na(s) ', end='')
for x in range(0, lista.count(min(lista))):
    print(f'{lista.index(min(lista), index_menor) + 1}', end='ª')
    print(', ' if x + 1 < lista.count(min(lista)) else '', end='')
    index_menor = lista.index(min(lista), index_menor) + 1

if lista.count(min(lista)) == 1:
    print(' posição', end='')
else:
    print(' posições', end='')