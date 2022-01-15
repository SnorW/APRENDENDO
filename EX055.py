lista_peso = []
for x in range(1, 6):
    peso = int(input('Digite seu peso por favor'))
    lista_peso.append(peso)

lista_peso.sort()
print('{}kg é o peso mais leve, {}kg é o peso mais pesado'.format(lista_peso[0], lista_peso[4]))
