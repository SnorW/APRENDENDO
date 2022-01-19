import time
# Código maior para deixar intuitivo
num = int(input('Digite um valor: '))
numeros = num - 2
soma_multiplicao_anterior = num * (num - 1)
soma_multiplicao_proxima = soma_multiplicao_anterior

print('Calulando {}!'.format(num))
time.sleep(0.8)
if num != 1:
    print('{} * {} = {}'.format(num, num - 1, soma_multiplicao_proxima))
elif num == 1:
    print('1 * 1 = 1')
while numeros > 0:
    if num != 1:
        time.sleep(0.4)
        soma_multiplicao_proxima *= numeros
        print('{} * {} = {}'.format(soma_multiplicao_anterior, numeros, soma_multiplicao_proxima))
        soma_multiplicao_anterior = soma_multiplicao_proxima
        numeros -= 1

if num != 1:
    time.sleep(0.8)
    print('O fatorial de {} é igual a {}'.format(num, soma_multiplicao_proxima))
elif num == 1:
    time.sleep(0.4)
    print('O fatorial de 1 é igual a 1')
