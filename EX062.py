ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = ptermo
loop = 0
user_termos = 10

while loop <= user_termos:
    print(pa)
    pa += razao
    loop += 1
    if loop == user_termos:
        pergunta = int(input('''Escolha uma opção
[1] Para mais termos
[2] Para parar'''))
        if pergunta == 1:
            perguntatermos = int(input('Quantos termos você deseja ver?'))
            user_termos += perguntatermos
        if pergunta == 2:
            print('Obrigado e fechando!')
            break
