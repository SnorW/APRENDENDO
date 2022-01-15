import time
from random import choice

while True:
    print('Vamos jogar Jo-Ken-Po!')
    jogadaplayer = input('Escolha papel, pedra ou tesoura!').strip().lower()
    opcao = ['pedra', 'papel', 'tesoura']
    jogadacomp = choice(opcao)

    if jogadaplayer == 'pedra' or jogadaplayer == 'tesoura' or jogadaplayer == 'papel':
        if jogadaplayer == jogadacomp:
            print('JO!')
            time.sleep(0.4)
            print('KEN!')
            time.sleep(0.4)
            print('PO!')
            time.sleep(0.3)
            print('-=' * 10)
            print('Você jogou {} e o computador jogou {}'.format(jogadaplayer.title(), jogadacomp.title()))
            print('Você ganhou!!')
            print('-=' * 10)
            time.sleep(0.4)
            tenta = input('Você deseja continuar jogando?').strip().lower()
            if tenta == 'sim' or tenta == 's':
                continue
            elif tenta == 'nao' or tenta == 'não' or tenta == 'n':
                print('Obrigado por jogar!')
                break
        elif jogadaplayer != jogadacomp:
            print('JO!')
            time.sleep(0.4)
            print('KEN!')
            time.sleep(0.4)
            print('PO!')
            time.sleep(0.3)
            print('-=' * 10)
            print('Você jogou {} e o computador jogou {}'.format(jogadaplayer.title(), jogadacomp.title()))
            print('Você perdeu...')
            print('-=' * 10)
            time.sleep(0.4)
            tenta = input('Você deseja continuar jogando?').strip().lower()
            if tenta == 'sim' or tenta == 's':
                continue
            elif tenta == 'nao' or tenta == 'não' or tenta == 'n':
                print('Obrigado por jogar!')
                break
    else:

        print('Jogada inválida')
        tenta = input('Deseja tentar novamente?').strip().lower()
        if tenta == 'sim' or tenta == 's':
            continue
        elif tenta == 'nao' or tenta == 'não' or tenta == 'n':
            print('Obrigado por jogar')
            break
