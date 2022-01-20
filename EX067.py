num = 0

while True:
    num = int(input('Digite um valor: '))
    if num > 0:
        for x in range(1, 11):
            print(f'{num} * {x} = {num * x}')
    else:
        print('Opção inválida')
        break
print('Programa finalizado, obrigado!')