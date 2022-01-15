from random import randint

perg = input('Você deseja jogar os dados?').strip().lower()

randint = randint(1, 6)

while perg == 'sim' or perg == 's':
    perg2 = int(input('Digite um numero de 1 a 6'))
    if 1 <= perg2 <= 6:
        print('O numero sorteado foi {}'.format(randint))
        perg3 = input('Você deseja tentar novamente?').strip().lower()
        if perg3 == 'nao' or perg3 == 'n' or perg3 == 'não':
            break
        elif perg3 == 'sim' or perg3 == 's':
            continue
    else:
        print('Numero inválido')
        perg3 = input('Você deseja tentar novamente?')

if perg != 'nao' and perg != 'não' and perg != 'n' and perg != 'sim' and perg != 's':
    print('Opção inválida , por favor digite Sim ou Não')

print('Quando quiser jogar, é só me rodar !!')
