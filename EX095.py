dados_jogadores = []
temp_jogadores = {}
gols = []

sim = ('sim', 's')
nao = ('nao', 'n', 'não')

condicao_while = True
while condicao_while:
    nome_input = str(input('Digite o nome do jogador: ')).strip()
    jogos_input = int(input('Quantos jogos ele jogou?: '))
    for x in range(0, jogos_input):
        gol = int(input(f'Quantos gols ele fez no {x+1}° jogo?'))
        gols.append(gol)
    temp_jogadores['Nome'] = nome_input
    temp_jogadores['Partidas jogadas'] = jogos_input
    temp_jogadores['Gols'] = gols[:]
    dados_jogadores.append(temp_jogadores.copy())
    temp_jogadores.clear()
    gols.clear()
    while True:
        tentar_nv = str(input('Deseja adicionar outro jogador? ')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, digite SIM ou NÃO')

print(f'{dados_jogadores}')
print('=-'*30)
print(f'{"Código":<5}', f'{"Nome":<10}', f'{"Gols":<15}', f'{"Total de gols":<20}')
for x in range(0, len(dados_jogadores)):
    print(f'{x+1:<5}', f'{dados_jogadores[x]["Nome"]:<10}', f'{str(dados_jogadores[x]["Gols"]):<15}', f'{sum(dados_jogadores[x]["Gols"]):<20}')

while True:
    print('=-'*30)
    perg = int(input('Digite o codigo do jogador para ver as suas informações (999 para fechar o programa)'))
    print('=-'*30)
    print(f'Levantamento do jogador {dados_jogadores[perg-1]["Nome"]}')
    if perg-1 in range(0, len(dados_jogadores)):
        for x in range(0, len(dados_jogadores[perg-1]["Gols"])):
            print(f'No jogo N°{x+1} fez {dados_jogadores[perg-1]["Gols"][x]}')
    elif perg == 999:
        break
    else:
        print(f'Jogador {perg} inválido!')
print('Programa finalizado, obrigado!')
