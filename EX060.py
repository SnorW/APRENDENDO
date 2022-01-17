from math import factorial
num1 = int(input('Digite um valor: '))
multiplicador = num1
fatorial = 0
resultado = 0

while multiplicador >= 2:
    multiplicador -= 1
    resultado = num1 * multiplicador
    print('{} * {} = {}'.format(num1, multiplicador, resultado))
    if fatorial == 0:
        fatorial = num1 * multiplicador
    elif fatorial > 0:
        fatorial *= multiplicador

print('O fatorial de {} é {}'.format(num1, fatorial))
print(factorial(num1))
