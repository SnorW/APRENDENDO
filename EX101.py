
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 0 < idade < 120:
        if idade < 16:
            return f'Com {idade} anos seu voto foi negado'
        elif idade < 18 or idade >= 65:
            return f'Com {idade} anos seu voto é opcional'
        else:
            return f'Com {idade} anos seu voto é obrigatório'
    else:
        if idade <= 0:
            return f'Um viajante no tempo! você nascerá daqui {idade} anos'
        elif idade >= 120:
            return f'Caraca temos uma múmia de {idade} anos aqui!'


ano_input = int(input('Digite o ano de nascimento: '))
print(voto(ano_input))
