lista_peso = []
for x in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa'.format(x)))
    lista_peso.append(peso)

lista_peso.sort()
print('{}kg é o mais leve, {}kg é o mais pesado'.format(lista_peso[0], lista_peso[len(lista_peso) - 1]))

print('A média de peso dessas 5 pessoas é {} '.format(sum(lista_peso) / len(lista_peso)))
