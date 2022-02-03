from time import sleep


def maior(*crescente):
    print('Analisando os dados')
    sleep(0.4)
    if len(crescente) > 0:
        print(crescente)
        print(f'Foram analisados {len(crescente)} valores e seu maior valor foi {max(crescente)}')
    else:
        print('Não existe dados para ser analisado')


