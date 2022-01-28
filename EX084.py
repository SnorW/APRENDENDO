pessoas_cadastradas = []
pessoas = []
pmais_pesadas = []
pmais_leves = []
sim = ('sim', 's')
nao = ('não', 'n', 'nao')

condicao_while = True
while condicao_while:
    nome_input = str(input('Digite o nome: '))
    peso_input = float(input('Digite o peso: '))
    pessoas.append(peso_input)
    pessoas.append(nome_input)
    pessoas_cadastradas.append(pessoas[:])
    pessoas.clear()
    while True:
        tentar_nv = str(input('Deseja adicionar mais pessoas? S/N')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, digite SIM ou NÃO')

pessoas_cadastradas.sort()
for nome_peso in pessoas_cadastradas:
    if nome_peso[0] == max(pessoas_cadastradas)[0]:
        pmais_pesadas.append(nome_peso)
    if nome_peso[0] == min(pessoas_cadastradas)[0]:
        pmais_leves.append(nome_peso)
print(f'Foram cadastradas {len(pessoas_cadastradas)} pessoas')
print(f'O maior peso foi de {pmais_pesadas[0][0]} KG de ', end='')
for x in range(0, len(pmais_pesadas)):
    print(f'{pmais_pesadas[x][1]}', end='')
    print(', ' if x+2 < len(pmais_pesadas) else ' ', end='')

print(f'\nO menor peso foi de {pmais_leves[0][0]} KG de ', end='')
for x in range(0, len(pmais_leves)):
    print(f'{pmais_leves[x][1]}', end='')
    print(', ' if x+2 < len(pmais_leves) else ' ', end='')
