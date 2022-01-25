palavras = ('Arroz', 'Feijao', 'Catorze', 'Vendido', 'Mandarim', 'Fisgado', 'Amuleto')

for x in range(0, len(palavras) - 1):
    print(f'\nA palavra {palavras[x]} tem as vogais: ', end='')
    for letra in palavras[x]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
