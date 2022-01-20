from datetime import date
ano_atual = date.today().year
# Contadores
anos18_cont = 0
sexomasc_cont = 0
menos20anos_cont = 0

condicaowhile = True

while condicaowhile:
    print('-='*50)
    idade = int(input('Por favor digite o ano que você nasceu'))
    sexo = str(input('Por favor digite seu sexo: M/F')).strip().lower()
    print('-='*50)
    if sexo in 'mf':
        if 0 < ano_atual - idade < 100:
            if ano_atual - idade > 18:
                anos18_cont += 1
            if sexo == 'm':
                sexomasc_cont += 1
            if sexo == 'f' and ano_atual - idade < 20:
                menos20anos_cont += 1
        else:
            print('Temos um viajante do tempo aqui!, por favor tente novamente')
    else:
        print('Não cadastrado, digite M para masculino ou F para feminino')
    while True:
        pergunta = str(input('Você deseja cadastrar mais uma pessoa?')).strip().lower()
        if pergunta == 'n' or pergunta == 'não' or pergunta == 'nao':
            condicaowhile = False
            break
        elif pergunta == 's' or pergunta == 'sim':
            break
        else:
            print('Opção inválida, digite sim ou não!')

print('-='*50)
print(f"""{anos18_cont} Pessoa(s) acima dos 18 anos
{sexomasc_cont} Homem(ns) cadastrado(s)
{menos20anos_cont} Mulher(es) com menos de 20 anos""")
print('-='*50)