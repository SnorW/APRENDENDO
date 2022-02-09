def notas(*n, situacao=False):
    """
    Função para mostrar o total de notas, maior nota, menor nota, nota média e situação em um dicionário
    :param n: Notas em um dicionário
    :param situacao: (opcional) Adiciona a situação no dicionário
    :return: Retorna o dicionário
    """
    media = sum(n)/len(n)
    notas_dict = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': f'{sum(n)/len(n):.2f}'}
    print(notas_dict)
    if situacao:
        if 5 > media >= 0:
            notas_dict['situacao'] = 'Ruim'
        elif 7 > media >= 5:
            notas_dict['situacao'] = 'Razoavel'
        elif 10 >= media >= 7:
            notas_dict['situacao'] = 'Bom'
    return notas_dict


notas(10, 1.4, 9, 4, 5.5, 5.3, 3.3, 8, 7.7, 9.9, situacao=False)
