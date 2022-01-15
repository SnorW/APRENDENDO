valorcasa = int(input('Digite o valor da casa'))
salario = int(input('Digite o seu salario'))
anos = int(input('Em quantos anos pretende pagar?'))
prestacao = valorcasa / (anos * 12)
salarioemanos = ((anos * 12) * salario)


if prestacao > salario * 0.30:
    print('Desculpe mas não será possivel aceitar o seu emprestimo')
    print('As prestações de R${:.2f} são maiores que 30% do seu salário que são: R${:.2f}'
          .format(prestacao, (salario * 0.30)))
else:
    print('Seu emprestimo será aprovado!')
    print('Você terá {:.0f} prestações de R${:.2f} da sua casa'.format(anos * 12,prestacao))
