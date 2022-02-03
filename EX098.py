from time import sleep


def contador(inicio, final, passo):
    seq_crescente = inicio
    seq_decrescente = inicio
    if inicio < final:
        for x in range(inicio, final+1):
            sleep(0.2)
            print(seq_crescente, end=' ')
            if seq_crescente <= final:
                seq_crescente += passo
                if seq_crescente > final:
                    break
            else:
                break
        print()
    elif inicio > final:
        if passo > 0:
            for x in range(final, inicio+1):
                sleep(0.2)
                print(seq_decrescente, end=' ')
                if seq_decrescente >= final:
                    seq_decrescente -= passo
                    if seq_decrescente < final:
                        break
                else:
                    break
            print()
        elif passo < 0:
            for x in range(final, inicio+1):
                sleep(0.2)
                print(seq_decrescente, end=' ')
                if seq_decrescente >= final:
                    seq_decrescente += passo
                    if seq_decrescente < final:
                        break
                else:
                    break
            print()
    print('=-='*30)


sim = ('s', 'sim')
nao = ('n', 'não', 'nao')

contador(0, 10, 1)
contador(10, 0, 2)

condicao_while = True
while condicao_while:
    inicio_input = int(input('Digite um valor natural para o inicio: '))
    final_input = int(input('Digite um valor natural para o final: '))
    passo_input = int(input('Digite um valor natural para o passo: '))
    contador(inicio_input, final_input, passo_input)
    while True:
        tentar_nv = str(input('Tentar novamente?')).lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, digite SIM ou NÃO por favor')

print('Programa finalizado!')
