lista_produtos = ('Café 500g', 8.0, 'Leite 1L', 5.0, 'Snickers 1Uni', 4.5, 'Queijo 1KG', 34.80, 'Manga 1KG', 4.99, 'Arroz 1KG',
                  12.75)
escalonamento_nome = 0
escalonamento_preco = 1

print('-'*60)
print(' '*15, 'LISTA DE PREÇOS DOS PRODUTOS')
print('-'*60)
for x in range(0, len(lista_produtos)):
    if lista_produtos[x - 1]:
        print(f'\n{lista_produtos[escalonamento_nome]:.<40}', end='')
        escalonamento_nome += 2
        print('R$', end=' ')
        print(f'{lista_produtos[escalonamento_preco]:>10.2f}', end='')
        escalonamento_preco += 2
        if escalonamento_preco > len(lista_produtos):
            break
print('\n')
print('-'*60)
