soma = 0
repeticao = True

while repeticao:
    num = int(input('Digite um numero ou digite 999 para finalizar o programa: '))
    if num != 999:
        print('{} + {} = {}'.format(num, soma, num + soma))
        soma += num
    elif num == 999:
        print('A soma de todos os numeros digitados foi {}'.format(soma))
        print('Programa finalizado, obrigado')
        repeticao = False
