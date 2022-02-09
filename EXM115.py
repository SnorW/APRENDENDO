def cadastrar():
    while True:
        try:
            nome = input('Digite seu nome: ')
            if not nome.isalpha():
                print('Preencha os campos corretamente!')
                continue
            idade = int(input('Digite sua idade: '))
        except:
            print('Preencha os campos corretamente!')
        else:
            file1 = open('EX115.txt', 'a')
            file1.write(f'\n{f"Nome: {nome}":<2}')
            file1.write(f'{f"{idade} anos":<50}')
            file1.close()
            break


def listar():
    file1 = open('EX115.txt', 'r')
    print('--' * 30)
    print(' '*20, 'Pessoas cadastradas')
    print(file1.read())
    file1.close()


def limpar():
    file1 = open('EX115.txt', 'w')
    file1.close()
