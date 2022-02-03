lista_pessoas = []
dict_pessoas = {}
lista_mulheres = []
lista_maioresmedia = []

idade = 0

fem = ('MULHER', 'FEMININO', 'F')
masc = ('MASCULINO', 'HOMEM', 'M')
sim = ('sim', 's')
nao = ('nao', 'n', 'não')


condicao_while = True
while condicao_while:
    nome_input = str(input('Digite seu nome: '))
    while True:
        sexo_input = str(input('Digite o seu sexo M/F: ')).upper()
        if sexo_input in masc or sexo_input in fem:
            break
        else:
            print('Opção inválida, digite M ou F')

    idade_input = int(input('Digite a sua idade: '))
    dict_pessoas['Nome'] = nome_input
    dict_pessoas['Sexo'] = sexo_input
    dict_pessoas['Idade'] = idade_input
    lista_pessoas.append(dict_pessoas.copy())
    idade += idade_input
    if sexo_input.upper().strip() in fem:
        lista_mulheres.append(nome_input)
    dict_pessoas.clear()
    while True:
        tentar_nv = str(input('Adicionar mais pessoas?')).lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, digite SIM ou NÃO')


print(f'A) Foram cadastradas o total de {len(lista_pessoas)} pessoas')
if len(lista_mulheres) > 0:
    print(f'B) As mulheres cadastradas foram: {lista_mulheres}')
else:
    print('B) Nenhuma mulher foi cadastrada')
print(f'C) A idade média entre as pessoas cadastradas é: {idade/len(lista_pessoas):.0f}')

for items in lista_pessoas:
    if idade/len(lista_pessoas) < items['Idade']:
        lista_maioresmedia.append(items)
if len(lista_maioresmedia) > 0:
    print(f'D) As pessoas maiores que a média de idade é/são:')
    for item in lista_maioresmedia:
        for k, v in item.items():
            print(f'    {k}: {v}', end=' ')
        print()
else:
    print('D) Não ouve pessoas maiores que a média de idade')
