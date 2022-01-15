from datetime import date
sexo = input('Você é do sexo masculino ou feminino?').strip().lower()
idade = int(input('Digite a sua idade'))
ano = date.today().year

if sexo == 'masculino':
    if idade > 18:
        v1 = idade - 18
        print('O tempo para você se alistar já venceu em {} ano(s)'.format(v1))
        print('Seu alistamento foi no ano de {}'.format(ano - v1))
    elif idade < 18:
        v1 = 18 - idade
        print('Falta {} ano(s) para você se alistar'.format(v1))
        print('Seu alistamento será no ano de {}'.format(ano + v1))
    elif idade == 18:
        print('Já está na hora de você se alistar!!')
elif sexo == 'feminino':
    print('Você que é do sexo feminino não precisará se alistar obrigatóriamente')
else:
    print('Sexo inválido')
