from datetime import date
ano = int(input('Digite o ano'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bisexto'.format(ano))
    print('Os proximos anos bisextos são: {} e {}'.format(ano + 4, ano + 8))
else:
    print('O ano de {} não é bisexto'.format(ano))



