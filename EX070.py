# Contadores
total_compra = 0
menor_valor = 19 * 1000
menor_nome = ''
valormaisde1000 = 0
# Condição
condicaowhile_principal = True

print('='*15, 'Bem-vindo ao menu da loja', '='*15)

while condicaowhile_principal:
    nome_produto = str(input('Digite o nome o produto: ')).strip().lower()
    valor_produto = float(input('Digite o valor do produto R$: '))
    total_compra += valor_produto
    print('=-' * 30)
    if valor_produto < menor_valor:
        menor_valor = valor_produto
        menor_nome = nome_produto
    if valor_produto >= 1000:
        valormaisde1000 += 1
    while True:
        novo_produto = str(input('Você quer adicionar novos produtos?')).strip().lower()
        print('=-' * 30)
        if novo_produto == 'sim' or novo_produto == 's':
            break
        elif novo_produto == 'n' or novo_produto == 'não' or novo_produto == 'nao':
            condicaowhile_principal = False
            break

print(f'''{total_compra:.2f} foi valor final dos produto(s)
{valormaisde1000} produto(s) com o valor maior que R$1000
{menor_nome.capitalize()} é o produto mais barato, no valor de {menor_valor}''')
