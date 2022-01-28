lista = []

for x in range(0, 5):
    valor = int(input('Digite um valor inteiro: '))
    if x == 0:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado na posição {x}')
    for pos in range(0, len(lista)):
        if valor > lista[pos]:
            if pos == 0:
                if valor > lista[len(lista)-1]:
                    lista.insert(len(lista), valor)
                    print(f'O valor {valor} foi adicionado na posição {len(lista) -1} (última posição)')
                    break
            if pos != 0:
                if valor > lista[len(lista)-pos]:
                    lista.insert(len(lista)-pos+1, valor)
                    print(f'O valor {valor} foi adicionado na posição {len(lista)-pos+1}')
                    break
        elif valor < lista[pos]:
            lista.insert(pos, valor)
            print(f'O valor {valor} foi adicionado na posição {pos}')
            break
        elif x != 0 and valor == lista[pos]:
            lista.insert(pos, valor)
            print(f'O valor {valor} foi adicionado na posição {pos}')
            break
print(f'O resultado da lista foi: {lista}')
