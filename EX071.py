print('='*15, 'Bem-vindo ao menu Banco IC', '='*15)
valor_sacado = int(input('Quantos reais você deseja sacar R$: '))
cont_notas_50 = 0
cont_notas_20 = 0
cont_notas_10 = 0
cont_notas_1 = 0

for x in range(1, 2):
    cont_notas_50 = valor_sacado // 50
    if valor_sacado % 50 >= 20:
        cont_notas_20 = (valor_sacado % 50) // 20
    if (valor_sacado % 50) % 20 >= 10:
        cont_notas_10 = (valor_sacado % 50 % 20) // 10
    if ((valor_sacado % 50) % 20) % 10 >= 1:
        cont_notas_1 = cont_notas_10 = (valor_sacado % 50 % 20 % 10) // 1

print(f'''Você receberá R${valor_sacado} em:
{cont_notas_50} Cédulas de R$50
{cont_notas_20} Cédulas de R$20
{(valor_sacado % 50 % 20) // 10} Cédulas de R$10
{cont_notas_1} Cédulas de R$1''')
