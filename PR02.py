from random import randint

n1 = int(input('Digite um numero'))
vmaximo = 10
vminimo = 1
valeatorio = randint(vminimo, vmaximo)

print(valeatorio)

while vmaximo >= n1 >= vminimo:
    if n1 == valeatorio:
        print('Parabéns você acertou!!')
        break
    elif n1 > valeatorio:
        print('Você chutou acima do valor')
        tente = int(input('Digite um numero para tentar novamente!'))
        if tente == valeatorio:
            print('Você acertou parabéns!')
            break
        elif tente > valeatorio:
            print('Você chutou acima!')
            continue
        elif tente < valeatorio:
            print('Você chutou abaixo')
            continue
    elif n1 < valeatorio:
        print('Você chutou abaixo do valor gerado!')
        tente = int(input('Digite outro numero para tentar novamente !'))
        if tente == valeatorio:
            print('Você acertou! Parabéns!')
            break
        elif tente < valeatorio:
            continue
        elif tente > valeatorio:
            print('Você chutou acima!')
