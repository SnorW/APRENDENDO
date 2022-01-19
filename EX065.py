repeticao = 2
loop = 0
soma = 0
lista_numeros = []

while loop < repeticao:
    num1 = int(input('Digite um valor: '))
    loop += 1
    soma += num1
    lista_numeros.append(num1)
    if loop == repeticao:
        print('A média entre esses valores foi {:.2f}'.format(soma / repeticao))
        pergunta = input('Você deseja adicionar mais valores?')
        if pergunta == 'sim' or pergunta == 's':
            repeticao += 2
        elif pergunta == 'n' or pergunta == 'nao' or pergunta == 'não':
            lista_numeros.sort()
            print('A média entre esses valores foi {:.2f}'.format(soma / repeticao))
            print('O maior valor foi {} e o menor valor foi {}'.format(lista_numeros[len(lista_numeros) - 1], lista_numeros[0]))
            print('Programa finalizado, obrigado')
        else:
            print('Opção inválida, digite sim ou não')
