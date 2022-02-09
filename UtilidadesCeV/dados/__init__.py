def lerdinheiro(a):
    if a.strip() != '':
        if a.replace(',', '').isnumeric() or a.replace('.', '').isnumeric():
            if a.find(','):
                return float(a.replace(',', '.'))
            else:
                return float(a)
        else:
            print(f'Digite um numero natural por favor')
    else:
        return 'Digite um numero por favor!'


def opcao_dinheiro(p):
    from UtilidadesCeV import moeda
    sim = ('sim', 's')
    nao = ('não', 'n', 'nao')
    format = False
    while True:
        n = int(input("""[0] Para aumentar
[1] Para diminuir
[2] Para o dobro
[3] Para a metade
[4] Para o resumo"""))
        while True:
            format_input = str(input('Deseja ver os valores formatados?')).strip().lower()
            if format_input in sim:
                format = True
                break
            elif format_input in nao:
                format = False
                break
            else:
                print('Opção inválida, digite SIM ou NÃO')
        if n in range(0, 5):
            if n == 0:
                ta = float(input('Digite um valor em % para aumentar: '))
                return print(f'{moeda.formatar(p, format)} aumentado em {ta}%: {moeda.aumentar(p, ta, format)}')
            elif n == 1:
                td = float(input('Digite um valor em % para diminuir: '))
                return print(f'{moeda.formatar(p, format)} diminuido em {td}%: {moeda.diminuir(p, td, format)}')
            elif n == 2:
                return print(f'{moeda.formatar(p, format)} dobrado: {moeda.dobro(p, format)}')
            elif n == 3:
                return print(f'{moeda.formatar(p, format)} dividido pela metade: {moeda.dobro(p, format)}')
            elif n == 4:
                ta = float(input('Digite um valor em % para aumentar: '))
                td = float(input('Digite um valor em % para diminuir: '))
                return moeda.resumo(p, ta, td, format)
        else:
            print('Escolha entre 0 e 4')
