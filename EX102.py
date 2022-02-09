
def fatorial(a, show=False):
    """
    Função para calcular o fatoria de a
    :param a: valor inteiro
    :param show: (opcional) mostra a conta do fatorial
    :return: a variavel f, que é o fatorial de a
    """
    coeficiente = a - 1
    f = a
    for x in range(0, a):
        result = f * coeficiente
        if show:
            if f == 1:
                print(f'1x1 = 1')
            else:
                print(f'{f}x{coeficiente} = {result}')
        coeficiente -= 1
        f = result
        if coeficiente == 0:
            break
    if not show:
        return print(f'{f}')


fatorial(4)

