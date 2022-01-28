# JEITO CORRETO DE SE FAZER, MINHAS TENTATIVAS ESTÃO NO EX078 EXTRA E EX078 EXTRAV2
lista = []
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

for x in range(0, 5):
    valor = int(input(f'Digite um valor para {x}ª posição: '))
    lista.append(valor)
    if x == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
            posicao_maior = x
        if valor < menor:
            menor = valor
            posicao_menor = x

print(f'Os valores digitados foram {lista}')
print(f'O maior valor foi {maior} que está na posição {posicao_maior}')
print(f'O menor valor foi {menor} que está na posição {posicao_menor}')
