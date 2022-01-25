lista = []
index_maior = 0
index_menor = 0

for v in range(1, 6):
    valor = int(input(f'Digite um valor para {v}ª Posição: '))
    lista.append(valor)

print(f'O maior valor {max(lista)} aparece nas posições: ', end='')
for index in range(1, 6):
    try:
        if lista.index(max(lista), index_maior, len(lista)) in range(len(lista)):
            print(f'{lista.index(max(lista), index_maior)+ 1}', end='ª ')
            index_maior = lista.index(max(lista), index_maior) + 1
    except:
        break
print(f'\nO menor valor {min(lista)} aparece nas posições: ', end='')
for index in range(1, 6):
    try:
        if lista.index(min(lista), index_menor, len(lista)) in range(len(lista)):
            print(f'{lista.index(min(lista), index_menor) + 1}', end='ª ')
            index_menor = lista.index(min(lista), index_menor) + 1
    except:
        break