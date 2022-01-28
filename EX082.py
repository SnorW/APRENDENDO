valores = []
valores_pares = []
valores_impares = []
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

for x in range(0, len(valores)):
    if valores[x] % 2 == 0 and valores[x] != 0:
        valores_pares.append(valores[x])
    elif valores[x] % 2 == 1:
        valores_impares.append(valores[x])

valores.sort()
valores_pares.sort()
valores_impares.sort()
print(f"""Os valores digitados foram: {valores}
Os valores pares digitados foram: {valores_pares}
Os valores impares digitados foram: {valores_impares}""")
