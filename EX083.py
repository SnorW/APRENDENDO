expressao = str(input('Digite uma expressão: ')).strip()
lista_expressao = expressao.replace('', ' ').split()
cont = 0

for x in range(0, len(lista_expressao)):
    if lista_expressao[x] == ')':
        cont += 1
    if lista_expressao[x] == '(':
        cont += 1
if cont % 2 == 0 and cont != 0:
    print(f'A expressão {expressao} é válida')
elif cont % 2 != 0 or cont == 0:
    print(f'A expressão {expressao} não é válida')
