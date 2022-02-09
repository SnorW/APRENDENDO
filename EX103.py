def ficha(nome='<desconhecido>', gols='0'):
    if not gols.isnumeric():
        gols = 0
    return f'O jogador {nome} fez {gols} gols'


n = str(input('Nome do jogador: '))
g = str(input('Gols: '))
print(ficha(n, g))
