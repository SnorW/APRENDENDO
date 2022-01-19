user_termos = int(input('Quantos termos você deseja mostrar?'))
loop = 0
fibonacci = 0
fibonacci_anterior = fibonacci

while loop <= user_termos:
    print(fibonacci, end='')
    print(' → ' if loop <= user_termos - 1 else '\n', end='')
    fibonacci += fibonacci_anterior
    fibonacci_anterior = fibonacci - fibonacci_anterior

    loop += 1
    if fibonacci == 0:
        fibonacci += 1
print('FIM!')
