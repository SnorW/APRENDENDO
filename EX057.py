resposta = ''

while resposta != 'm' and resposta != 'f':
    pergunta = input('Digite o sexo M/F: ').strip().lower()
    resposta = pergunta

print('Você digitou o sexo {}'.format(resposta.capitalize()))

