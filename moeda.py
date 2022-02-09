def aumentar(p, t, format=False):
    """
    Função para aumentar p através de t %
    :param p: valor a ser aumentado
    :param t: taxa % que irá aumentar
    :param format: (opcional) Retorna formatado em R$
    :return: retorna p + t% de p
    """
    result = (t/100) * p + p
    if format:
        return formatar(result)
    else:
        return result


def diminuir(p, t, format=False):
    """
    Função para diminuir p por t %
    :param p: valor a ser diminuido
    :param t: taxa em % para diminuir
    :param format: (opcional) Retorna formatado em R$
    :return: retona p - t% de p
    """
    result = p - p * (t/100)
    if format:
        return formatar(result)
    else:
        return result


def dobro(p, format=False):
    """
    Função para dobrar p
    :param p: valor para ser dobrado
    :param format: (opcional) Retorna formatado em R$
    :return: retorna p dobrado
    """
    dobrop = p * 2
    if format:
        return formatar(dobrop)
    else:
        return dobrop


def metade(p, format=False):
    """
    Função para diminuir pela metade o valor p
    :param p: valor a ser diminuido pela metade
    :param format: (opcional) Retorna formatado em R$
    :return: retorna a metade de p
    """
    metadep = p / 2
    if format:
        return formatar(metadep)
    else:
        return metadep


def formatar(p, format=False):
    """
    Função para formatar p em R$
    :param p: valor a formatar
    :param format: (opcional) Para formatar
    :return: p
    """
    if not format:
        p_frmt = f'{p:.2f}'
        p_str = str(p_frmt).replace('.', ',')
        return f'R${p_str}'


def resumo(p, ta, td, format=False):
    """
    Função para mostrar o resumo
    :param p: valor a mostrar
    :param ta: taxa de aumento (em %)
    :param td: taxa de diminuição (em %)
    :param format: (opcional) mostra o resumo formatado para R$
    :return:
    """
    if format:
        aumentado = aumentar(p, ta, True)
        diminuido = diminuir(p, td, True)
        dobrado = dobro(p, True)
        metadedep =metade(p, True)
    else:
        aumentado = aumentar(p, ta)
        diminuido = diminuir(p, td)
        dobrado = dobro(p)
        metadedep = metade(p)
    print('-' * 46)
    print(' '*8, f'{"RESUMO DO VALOR":^19} {formatar(p)}')
    print('-' * 46)
    print(f'{"Preço analisado":<2}', f'{formatar(p):>15}')
    print(f'{f"Aumentado {ta}%":<2}', f'{aumentado:>15}')
    print(f'{f"Diminuido {td}%":<2}', f'{diminuido:>15}')
    print(f'{f"O dobro de {p} ":<2}', f'{dobrado:>15}')
    print(f'{f"A metade de {p} ":<2}', f'{metadedep:>15}')
