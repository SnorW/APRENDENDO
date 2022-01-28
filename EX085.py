lista_numeros = [[], []]
for x in range(0, 7):
    numeros = int(input('Digite um valor: '))
    if numeros % 2 == 0:
        lista_numeros[0].append(numeros)
    elif numeros % 2 == 1:
        lista_numeros[1].append(numeros)

print(f'Em ordem crescente dos numeros pares digitados foram: {lista_numeros[0]}')
print(f'Em ordem crescente dos numeros impáres digitados foram: {lista_numeros[1]}')
