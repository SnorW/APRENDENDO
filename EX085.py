lista_numeros = [[], []]
for x in range(0, 7):
    numeros = int(input(f'Digite o {x+1}° valor: '))
    if numeros % 2 == 0:
        lista_numeros[0].append(numeros)
    elif numeros % 2 == 1:
        lista_numeros[1].append(numeros)

lista_numeros[0].sort()
lista_numeros[1].sort()
print(f'Em ordem crescente dos numeros pares digitados foram: {lista_numeros[0]}')
print(f'Em ordem crescente dos numeros impáres digitados foram: {lista_numeros[1]}')
