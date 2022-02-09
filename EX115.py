import EXM115
from time import sleep

sim = ('sim', 's')
nao = ('n', 'não', 'nao')

condicao_while = True
while condicao_while:
    print('--'*30)
    print(("""[1] Para ver a ficha de pessoas cadastradas
[2] Para cadastrar nova pessoa
[3] Para limpar a ficha
[4] Para sair do sistema """))
    print('--'*30)
    opcao_input = int(input('Sua opção: '))
    if opcao_input in range(1, 5):
        if opcao_input == 1:
            sleep(0.2)
            EXM115.listar()
        elif opcao_input == 2:
            EXM115.cadastrar()
            sleep(0.4)
            print('Cadastrado com sucesso!')
        elif opcao_input == 3:
            EXM115.limpar()
            sleep(0.4)
            print('Ficha limpa!')
        elif opcao_input == 4:
            break
    else:
        print('Opção inválida!')

print('\nPrograma finalizado!')
