from random import randint

soma = 0
cont_jogador = 0

print('Vamos jogar par ou ímpar')
while True:
    jogador_opcao = str(input('Par ou ímpar?')).strip().lower()
    jogador = int(input('Digite um numero: '))
    comp = randint(1, 20)
    soma = comp + jogador
    print('=-' * 30)
    print(f'Você jogou {jogador} e o computador {comp}')
    if soma % 2 == 1:
        print(f'{soma} é ímpar')
        print('=-' * 30)
        if jogador_opcao != 'impar':
            print('Você perdeu!')
            break
    elif soma % 2 == 0:
        print(f'{soma} é par')
        print('=-' * 30)
        if jogador_opcao != 'par':
            print('Você perdeu!')
            break
    cont_jogador += 1

print(f'Você ganhou {cont_jogador} vezes')