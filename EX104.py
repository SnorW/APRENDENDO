def leiaint(perg):
    while True:
        n_input = input(perg)
        if n_input.isnumeric():
            return int(n_input)
        else:
            print('Erro, numero inválido!')


n = leiaint('Digite um numero inteiro: ')
print(f'Você digitou o numero {n}')
print(type(n))
