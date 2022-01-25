lista = []
sim = ('sim', 's')
nao = ('não', 'n', 'nao')

condicao_while = True

while condicao_while:
    valor = int(input('Digite um valor inteiro: '))
    if lista.count(valor) == 0:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado na lista')
    else:
        print('Esse número já existe dentro da lista!')
    while True:
        tentar_nv = str(input('Deseja adicionar outro numero?'))
        if tentar_nv.lower() in sim:
            break
        if tentar_nv.lower() in nao:
            condicao_while = False
            break

lista.sort()
if len(lista) > 1:
    print(f'Os valores digitados foram {lista:}')
else:
    print(f'O valor digitado foi {lista:}')
