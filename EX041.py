from datetime import date

ano = date.today().year
nascimento = int(input('Digite o ano de nascimento:'))
idade = ano - nascimento

print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Você é um nadador Mirim')
elif 9 < idade <= 14:
    print('Você é um nadador Infantil')
elif 14 < idade <= 19:
    print('Você é um nadador Junior')
elif 19 < idade <= 20 :
    print('Você é um nadador Senior')
elif idade > 20:
    print('Você é um nadador Master')
