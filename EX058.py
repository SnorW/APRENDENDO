from random import randint
nrandom = randint(1, 10)
user_resposta = 0
user_palpites = []
user_cont = 0
print(nrandom)

while user_resposta != nrandom:
    pergunta = int(input('Digite um numero de 1 a 10: '))
    user_resposta = pergunta
    user_cont += 1
    user_palpites.append(pergunta)
    if pergunta != nrandom:
        print('Você errou, tente novamente!')

palpites = str(user_palpites)
','.join(palpites)
print('Parabéns você acertou com {} tentativas'.format(user_cont))
print('O numero sorteado foi {}'.format(user_resposta, nrandom))
print(user_palpites)
