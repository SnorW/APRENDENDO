import time
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = ptermo
loop = 1

while loop <= 10:
    print(pa)
    pa += razao
    loop += 1
    time.sleep(0.3)
