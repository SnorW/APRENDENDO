
idademedia = 0
lista_idadehomem = []
idademulher21 = 0

rang = 5
for x in range(1, rang):
    nome = input('Digite seu nome').strip()
    idade = int(input('Digite sua idade'))
    idademedia += idade
    sexo = input('Digite o sexo').strip().lower()
    if sexo != 'masculino' and sexo != 'feminino':
        print('Sexo inválido!')
        print('Rode o programa novamente!')
        break
    elif sexo == 'masculino':
        print('{} é homem!'.format(nome))
        lista_idadehomem.append(idade)
        lista_idadehomem.sort()
    elif sexo == 'feminino':
        if idade < 21:
            idademulher21 += 1

print('A idade média é de {}'.format(idademedia / (rang - 1)))
if len(lista_idadehomem) >= 0:
    print('O homem mais velho tem {}'.format(lista_idadehomem[len(lista_idadehomem) - 1]))

if idademulher21 != 0:
    print('Existe {} mulher menores de 21 anos'.format(idademulher21))
else:
    print('Não existe mulheres menores de 21 anos')
