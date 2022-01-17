condicao = 0

while condicao == 0:
    num1 = int(input('Digite o primeiro valor'))
    num2 = int(input('Digite o segundo valor'))
    pergunta = int(input('''Escolha uma opção:
[1] Para somar
[2] Para multiplicar
[3] Para saber o maior valor
[4] Para novos valores
[5] Para sair'''))
    if pergunta == 1:
        print('A soma dos valores {} e {} é igual a {}'.format(num1, num2, num1 + num2))
    elif pergunta == 2:
        print('A multiplicação entre os valores {} e {} é igual a {}'.format(num1, num2, num1 * num2))
    elif pergunta == 3:
        if num1 > num2:
            print('O valor {} é maior que o valor {}'.format(num1, num2))
        elif num2 > num1:
            print('O valor {} é maior que o valor {}'.format(num2, num1))
    elif pergunta == 4:
        continue
    elif pergunta == 5:
        print('Obrigado e saindo!')
        condicao += 1
