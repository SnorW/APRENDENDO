nota1 = float(input('Digite uma nota'))
nota2 = float(input('Digite outra nota'))
media = (nota1 + nota2)/2
notaminima = 5.0
notamedia = 7.0

if media < notaminima:
    print('Você está reprovado com a média de {:.2f}!'.format(media))
elif notaminima <= media < notamedia:
    print('Você está em recuperação com a média de {:.2f}!'.format(media))
elif media >= notamedia:
    print('Você está aprovado com a média de {:.2f}'.format(media))
