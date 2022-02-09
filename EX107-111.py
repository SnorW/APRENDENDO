from UtilidadesCeV import moeda

sim = ('sim', 's')
nao = ('n', 'não', 'nao')

condicao_while = True
while condicao_while:
    p_input = str(input('Digite o valor: R$ ')).strip().lower()
    frmt = False
    if p_input == 'fim':
        condicao_while = False
        break
    if p_input.isnumeric():
        p = float(p_input)
        while True:
            perg = input("""[0] Para aumentar
[1] Para diminuir
[2] Para mostrar dobro
[3] Para mostrar a metade
[4] Para resumir""")
            frmt_input = str(input('Deseja o numero formatado?')).strip().lower()
            if frmt_input in sim:
                frmt = True
            elif frmt_input in nao:
                frmt = False
            else:
                print('Digite sim ou não por favor!')
            if perg.isnumeric():
                if int(perg) in range(0, 5) and frmt_input in sim or frmt_input in nao:
                    break
                elif not int(perg) in range(0, 5):
                    print('Escolha entre 0 a 3')
            else:
                print('Opção inválida, escolha entre 0 e 3')
        if int(perg) == 0:
            t = float(input('Digite um valor para taxa %: '))
            print(f'O valor {moeda.formatar(p)} aumentado em {t}% é igual á: {moeda.aumentar(p, t, format=frmt)}')
        elif int(perg) == 1:
            t = float(input('Digite um valor para taxa %: '))
            print(f'O valor {moeda.formatar(p)} diminuido em {t}% é igual á:{moeda.diminuir(p, t, format=frmt)}')
        elif int(perg) == 2:
            print(f'O valor {moeda.formatar(p)} dobrado é igual á: {moeda.dobro(p, format=frmt)}')
        elif int(perg) == 3:
            print(f'O valor {moeda.formatar(p)} cortado pela metade é igual á: {moeda.metade(p, format=frmt)}')
        elif int(perg) == 4:
            taumento = float(input('Digite um valor para aumentar (em %): '))
            treducao = float(input('Digite um valor para diminuir (em %): '))
            print(moeda.resumo(p, taumento, treducao, frmt))
    else:
        print('Digite um numero natural!')

print('Programa finalizado!')
