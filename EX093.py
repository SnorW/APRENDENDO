
aproveitamento = []
aproveitamento_dict = {}

nome_input = str(input('Nome do jogador: '))
partidas_input = int(input('Numero de partidas jogadas: '))
gols = []

# Contadores
cont = 1
total_gols = 0

for x in range(0, partidas_input):
    gols_input = int(input(f'Quantos gols ele fez no {x+1}° jogo?'))
    gols.append(gols_input)

aproveitamento_dict['Nome'] = nome_input
aproveitamento_dict['Partidas jogadas'] = partidas_input
aproveitamento_dict['Gols'] = gols
aproveitamento.append(aproveitamento_dict)

print('=-'*30)
print(aproveitamento)
print('=-'*30)
for items in aproveitamento:
    for k, v in items.items():
        print(f'{k} tem o valor: {v}')

print('=-'*30)
print(f'O jogador {aproveitamento[0]["Nome"]} jogou {aproveitamento[0]["Partidas jogadas"]} jogos')
for v in aproveitamento[0]['Gols']:
    print(f'Na {cont}ª partida ele fez {v} gols')
    cont += 1
    total_gols += v
print(f'O total de gols foi {total_gols}')