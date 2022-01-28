valores =[]
sim = ('sim', 's')
nao = ('não', 'n', 'nao')
condicao_while = True

while condicao_while:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    while True:
        tentar_nv = str(input('Deseja tentar novamente? S/N')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, por favor digite Sim ou Não')

valores.sort(reverse=True)
print(f'Você digitou {len(valores)} valores')
print(f'Os valores digitados em ordem decrescente é: {valores}')

if valores.count(5) > 0:
    print(f'O numero 5 foi digitado {valores.count(5)} vezes e aparece primeiro na posição {valores.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')
