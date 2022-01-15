import datetime
pdmaior = 0
pdmenor = 0

for x in range(1, 8):
    idade = int(input('Qual o ano de nascimento?'))
    if 21 <= (datetime.date.today().year - idade):
        pdmaior += 1

    elif 21 > (datetime.date.today().year - idade):
        pdmenor += 1

print('{} Pessoas são maiores de idade (21 anos)'.format(pdmaior))
print('{} Pessoas são menores de idade (21 anos)'.format(pdmenor))
