pergunta = input('Digite o sexo M/F: ').strip().lower()

while pergunta not in 'mf':
    pergunta = input('Dados inválidos, digite novamente M/F')

print('Você digitou o sexo {}'.format(pergunta.capitalize()))
