from time import sleep


def pyhelp(cmd):
    print('~'*30)
    print(f'Acessando o manual do {cmd}')
    print('~' * 30)
    sleep(0.4)
    print(help(cmd))


while True:
    print('~'*30)
    print(f'Menu Pyhelp')
    print('~' * 30)
    cmd_input = str(input('Função ou Bíblioteca: ')).strip().lower()
    if cmd_input == 'fim':
        break
    else:
        pyhelp(cmd_input)

print('Programa finalizado!')