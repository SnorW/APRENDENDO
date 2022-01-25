tabela_brasileiro = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
                     'América Mineiro', 'Atlétio-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athlétio-PR',
                     'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
tabela_brasileiro_alfabetica = sorted(tabela_brasileiro)

print('5 Primeiros colocados:')
for pos in range(0, 5):
    print(f'{pos + 1}. {tabela_brasileiro[pos]}')

print('-='*30)
print('4 Últimos colocados:')
for pos in range(1, 5):
    print(f'{len(tabela_brasileiro) + 1 - pos}. {tabela_brasileiro[-pos]}')

print('=-'*30)
print('A chapecoense está {}° posição'.format(tabela_brasileiro.index('Chapecoense') + 1))


print('=-'*30)
print('Os times em órdem alfabética: ')
for pos in range(0, len(tabela_brasileiro)):
    print(tabela_brasileiro_alfabetica[pos], end='')
    print(', ' if pos < len(tabela_brasileiro_alfabetica) else'', end='')
