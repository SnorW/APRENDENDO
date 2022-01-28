lista_alunos_notas = []
alunosenotas = []
notas = []

sim = ('sim', 's')
nao = ('não', 'n', 'nao')


condicao_while = True
while condicao_while:
    nome_input = str(input('Digite o nome do aluno: '))
    nota1_input = float(input('Digite a 1ª nota: '))
    nota2_input = float(input('Digite a 2ª nota: '))
    notas.append(nota1_input)
    notas.append(nota2_input)
    alunosenotas.append(nome_input)
    alunosenotas.append(notas[:])
    alunosenotas.append((nota1_input + nota2_input) / 2)
    lista_alunos_notas.append(alunosenotas[:])
    while True:
        tentar_nv = str(input('Deseja adicionar mais alunos?')).strip().lower()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
    notas.clear()
    alunosenotas.clear()

print('-'*25)
print(f'{"No.":<5}', f'{"Nome":^5}', f'{"Média":>15}')
for x in range(0, len(lista_alunos_notas)):
    print(f'{x:<5}', f'{lista_alunos_notas[x][0]:^5}', f'{lista_alunos_notas[x][2]:>15.2f}')

condicao_while = True
while condicao_while:
    pos_aluno_input = int(input('Digite o numero do aluno para saber as suas notas ou digite 999 para interromper'))
    if pos_aluno_input == 999:
        break
    else:
        print(f'As notas de {lista_alunos_notas[pos_aluno_input][0]} são: {lista_alunos_notas[pos_aluno_input][1][0:]}')

print('Programa finalizado!')
