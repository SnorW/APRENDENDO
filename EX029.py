velocidade = int(input('Velocidade do carro'))

print('Sua velocidade é de {} KM/H'.format(velocidade))
if velocidade > 80:

    print('Você ultrapassou o limite de 80 KM/H e foi multado em {} reais'.format((velocidade - 80) * 7))
else:
    print('Boa viagem e preste atenção no limite de velocidade!')