bcoinpd = float(input('Bcoin por dia :'))
valorbcoinbrl = float(input('Valor do bcoin em brl : '))
bcoinsemana = bcoinpd * 7
bcoinmes = bcoinpd * 30
brldia = bcoinpd * valorbcoinbrl
brlsemana = bcoinsemana * valorbcoinbrl
brlmes = bcoinmes * valorbcoinbrl

print("""{} Bcoins por dia, {} BRL por dia
{} Bcoins por semana, {} BRL por semana
{} Bcoins por mês, {} BRL por mês""".format(bcoinpd, brldia, bcoinsemana, brlsemana, bcoinmes, brlmes))
