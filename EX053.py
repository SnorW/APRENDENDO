frase = input('Digite uma frase')
ffrase = frase.strip().lower().replace(" ", "")
addspaces = ' '.join(frase)
swaptolist = addspaces.split()
add = 0
remove = 0


for x in range(len(swaptolist)):
    if remove == add < len(swaptolist) and swaptolist[(0 + add)] == swaptolist[((len(swaptolist) - 1) - remove)]:
        add += 1
        remove -= 1
        print('{} é um palindromo'.format(frase.capitalize()))

    elif remove == add < len(swaptolist) and swaptolist[(0 + add)] != swaptolist[((len(swaptolist) - 1) - remove)]:
        print('não é palindromo')
        break
