# Ponto de quebra
pointbreak = 0
# Dados
idademedia = 0
lista_idadehomem = []
maioridadehomem = 0
nomehomem = ''
idademulher21 = 0
lista_nomemulher = []
# Variável de alcance 'Range'
rang = 5
for x in range(1, rang):
    nome = input('Digite o nome da {}ª pessoa: '.format(x)).strip()
    idade = int(input('Digite a idade da {} pessoa: '.format(x)))
    idademedia += idade
    sexo = input('Digite o sexo da {}ª pessoa: '.format(x)).strip().lower()
    if sexo != 'masculino' and sexo != 'm' and sexo != 'feminino' and sexo != 'f':
        print('Sexo inválido!')
        print('Rode o programa novamente!')
        pointbreak += 1
        break
    elif sexo == 'masculino' or sexo == 'm':
        lista_idadehomem.append(idade)
        lista_idadehomem.sort()
        if sexo in 'mmasculino' and idade > maioridadehomem:
            maioridadehomem = idade
            nomehomem = nome
    elif sexo == 'feminino' or sexo == 'f':
        if idade < 21:
            idademulher21 += 1
            lista_nomemulher.append(nome)

nomejuntomulher = ', '.join(lista_nomemulher)
if pointbreak == 0:
    print('A idade média é de {} anos'.format(idademedia / (rang - 1)))
    if len(lista_idadehomem) > 0:
        print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomehomem))

    if idademulher21 != 0:
        print('Existe {} mulher(es) menor(es) de 21 anos'.format(idademulher21))
        print('{} é/são menor(es) de 21 anos'.format(nomejuntomulher))
    else:
        print('Não existe mulher(es) menor(es) de 21 anos')
