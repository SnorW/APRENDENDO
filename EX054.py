import datetime
pdmaior = 0
pdmenor = 0
imortal = 0
futuro = 0

for x in range(1, 8):
    idade = int(input('Em que ano nasceu a {}° pessoa?'.format(x)))
    if 21 <= (datetime.date.today().year - idade) < 110:
        pdmaior += 1
    elif 21 > (datetime.date.today().year - idade) > 0:
        pdmenor += 1
    elif 100 < (datetime.date.today().year - idade):
        imortal += 1
    elif idade >= datetime.date.today().year:
        futuro += 1

print('{} Pessoas são maiores de idade (21 anos)'.format(pdmaior))
print('{} Pessoas são menores de idade (21 anos)'.format(pdmenor))

if imortal > 0:
    print('{} Pessoas são imortais ! (Acima de 110 anos)'.format(imortal))
if futuro > 0:
    print('{} Pessoas voltaram do futuro! (Ainda irão nascer)'.format(futuro))