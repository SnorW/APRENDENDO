pessoas_cadastradas = []
pessoas = []
sim = ('sim', 's')
nao = ('não', 'n', 'nao')

condicao_while = True
while condicao_while:
    nome_input = str(input('Digite o nome: '))
    peso_input = float(input('Digite o peso: '))
    pessoas.append(nome_input)
    pessoas.append(peso_input)
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
len_par = int(len(pessoas_cadastradas) / 2)
len_impar = int((len(pessoas_cadastradas) - 1) / 2)
print(f'Foram cadastradas {len(pessoas_cadastradas)} pessoas')
if len(pessoas_cadastradas) % 2 == 0:
    print(f'As pessoas mais pesadas foram{pessoas_cadastradas[:len_par]}')
    print(f'As pessoas mais leves foram{pessoas_cadastradas[len_par:]}')
else:
    print(f'As pessoas mais pesadas foram{pessoas_cadastradas[len_impar:]}')
    print(f'As pessoas mais leves foram{pessoas_cadastradas[:len_impar]}')



