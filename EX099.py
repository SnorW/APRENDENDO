from time import sleep


def maior(*crescente):
    print('Analisando os dados')
    sleep(0.4)
    if len(crescente) > 0:
        if len(crescente[0]) > 0:
            print(crescente[0])
            print(f'Foram analisados {len(crescente[0])} valores e o maior valor analisado foi {max(crescente[0])}')
    else:
        print('Não existe dados para ser analisado')


num_lista = []
sim = ('sim', 's')
nao = ('não', 'nao', 'n')

condicao_while = True
while condicao_while:
    num_input = float(input('Digite um numero natural: '))
    num_lista.append(num_input)
    while True:
        tentar_nv = str(input('Deseja adicionar outro numero?')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, por favor digite SIM ou NÃO')

maior(num_lista)
maior()
