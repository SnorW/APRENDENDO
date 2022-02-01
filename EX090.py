lista_alunos = []
dict_aluno = {}

sim = ('sim', 's')
nao = ('nao', 'n', 'não')

condicao_while = True
while condicao_while:
    dict_aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().lower().capitalize()
    dict_aluno['Média'] = float(input('Digite a média do aluno: '))
    if dict_aluno['Média'] >= 7:
        dict_aluno['Situação'] = 'Aprovado'
    elif dict_aluno['Média'] < 7:
        dict_aluno['Situação'] = 'Reprovado'
    lista_alunos.append(dict_aluno.copy())
    dict_aluno.clear()
    while True:
        tentar_nv = str(input('Quer adicionar mais alunos?')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, digite SIM ou NÃO')
for x in range(0, len(lista_alunos)):
    for k, v in lista_alunos[x].items():
        print(f'{k:}: {v:}', end=' ')
    print()