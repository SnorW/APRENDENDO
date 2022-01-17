frase = input('Digite uma frase')
junto = frase.strip().lower().replace(" ", "")
addspaces = ' '.join(frase)
swaptolist = addspaces.split()
inverso = ''

print(frase.capitalize())
for x in range(len(swaptolist)-1, -1, -1):
    print(swaptolist[x], end='')
    inverso += swaptolist[x]
if junto == inverso:
    print('\n{} é um palindromo'.format(frase.capitalize()))
else:
    print('\n{} não é um palindromo'.format(frase.capitalize()))
