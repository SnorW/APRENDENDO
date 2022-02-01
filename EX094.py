lista_pessoas = []
dict_pessoas = {}
lista_mulheres = []
lista_maioresmedia = []

idade = 0

fem = ('mulher', 'feminino', 'f')
sim = ('sim', 's')
nao = ('nao', 'n', 'não')

condicao_while = True
while condicao_while:
    nome_input = str(input('Digite seu nome: '))
    sexo_input = str(input('Digite o seu sexo M/F: '))
    idade_input = int(input('Digite a sua idade: '))
    dict_pessoas['Nome'] = nome_input
    dict_pessoas['Sexo'] = sexo_input
    dict_pessoas['Idade'] = idade_input
    lista_pessoas.append(dict_pessoas.copy())
    idade += idade_input
    if sexo_input.lower().strip() in fem:
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


print(lista_pessoas)
print(f'As mulheres cadastradas foram: {lista_mulheres}')
print(f'A idade média entre as pessoas cadastradas é: {idade/len(lista_pessoas):.2f}')

for items in lista_pessoas:
    if idade/len(lista_pessoas) < items['Idade']:
        lista_maioresmedia.append(items['Nome'])
print(f'As pessoas maiores que a média de idade é/são: {lista_maioresmedia}')