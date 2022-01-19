num1 = int(input('Digite um valor'))
loop = 0
numatual = num1
numanterior = 0
repeticao = 10

while loop < repeticao:
    print(numatual, end='')
    print(' → ' if loop < repeticao - 1 else '', end='')
    numatual += numanterior
    numanterior = numatual - numanterior
    loop += 1
    if loop == repeticao:
        pergunta = input('\nVocê ver mais numeros dessa sequencia, S/N?').strip().lower()
        if pergunta == 's' or pergunta == 'sim':
            perguntarepeticao = int(input('Quantos numeros você deseja ver a mais dessa sequencia?'))
            repeticao += perguntarepeticao
        elif pergunta == 'n' or pergunta == 'não' or pergunta == 'nao':
            print('Programa finalizado, obrigado')
        else:
            print('Opção invalida, por favor digite sim ou não')
