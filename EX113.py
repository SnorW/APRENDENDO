def leiaint():
    while True:
        try:
            a = int(input('Digite um valor inteiro: '))
        except (ValueError, TypeError):
            print('Erro, digite um numero inteiro por favor')
        else:
            return a


def leiafloat():
    while True:
        try:
            a = float(input('Digite um valor natural: '))
        except (ValueError, TypeError):
            print('Erro, digite um numero natural por favor')
        else:
            return a

print(leiaint())
print(leiafloat())