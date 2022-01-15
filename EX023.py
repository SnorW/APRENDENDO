num = input('Digite um numero de 0 a 9999')
numstrip = num.strip()
uni = numstrip[3]
dez = numstrip[2]
cen = numstrip[1]
mil = numstrip[0]
print("""{} Unidade[s]
{} Dezena[s] 
{} Centena[s] 
{} Milhare[s] """.format(uni, dez, cen, mil))
