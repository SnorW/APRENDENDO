import time
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = ptermo
loop = 0
user_termos = 10

while loop <= user_termos:
    time.sleep(0.4)
    print(pa, end='')
    print(' → ' if loop < user_termos - 1 else '', end='')
    pa += razao
    loop += 1
    if loop == user_termos:
        time.sleep(0.6)
        pergunta = int(input('''\nEscolha uma opção
[1] Para mais termos
[2] Para parar'''))
        if pergunta == 1:
            perguntatermos = int(input('Quantos termos você deseja ver?'))
            user_termos += perguntatermos
            if perguntatermos == 0:
                user_termos = False
        if pergunta == 2:
            time.sleep(0.6)
            print('Obrigado e fechando!')
            user_termos = False

time.sleep(0.6)
print('O Programa foi finalizado com {} termos mostrados'.format(loop))
