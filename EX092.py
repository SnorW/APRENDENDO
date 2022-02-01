from datetime import date

dados = []
dados_dict = {}

# EXEC
ano_input = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano_input
nome_input = str(input('Digite o seu nome:'))
carteira_input = int(input('Digite sua carteira de trabalho'))
dados_dict['Nome'] = nome_input
dados_dict['Idade'] = idade
dados_dict['Carteira'] = carteira_input
if carteira_input != 0:
    anocontrato_input = int(input('Em que ano foi contratado?'))
    salario_input = float(input('Qual o salário?'))
    aposentadoria = anocontrato_input + 35
    dados_dict['Contrato'] = anocontrato_input
    dados_dict['Salário'] = salario_input
    dados_dict['Ano de aposentadoria'] = aposentadoria
dados.append(dados_dict.copy())
dados_dict.clear()

for items in dados:
    for key, value in items.items():
        print(f'{key} é: {value}')
