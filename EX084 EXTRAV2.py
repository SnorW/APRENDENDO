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
    pessoas_cadastradas.sort()
    if peso_input == max(pessoas_cadastradas)[0]:
        pmais_pesadas.append(nome_input)
    elif peso_input > max(pessoas_cadastradas)[0]:
        pmais_pesadas.clear()
        pmais_pesadas.append(nome_input)
    if peso_input == min(pessoas_cadastradas)[0]:
        pmais_leves.append(nome_input)
    elif peso_input < min(pessoas_cadastradas)[0]:
        pmais_leves.clear()
        pmais_leves.append(nome_input)
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

print(f'Foram cadastradas {len(pessoas_cadastradas)} pessoas')
print(f'O maior peso foi de {max(pessoas_cadastradas)[0]} KG de {pmais_pesadas} ')
print(f'O menor peso foi de {min(pessoas_cadastradas)[0]} KG de {pmais_leves}')
