def area(larg, comp):
    area_resultado = larg * comp
    print(f'A area desse retangulo {larg}x{comp} é {area_resultado:.2f} cm²')


sim = ('s', 'sim')
nao = ('nao', 'n', 'não')

condicao_while = True
while condicao_while:
    larg_input = float(input('Digite a largura em cm: '))
    comp_input = float(input('Digite o comprimento em cm: '))
    area(larg_input, comp_input)
    while True:
        tentar_nv = str(input('Tentar novamente?')).lower().strip()
        if tentar_nv in sim:
            break
        elif tentar_nv in nao:
            condicao_while = False
            break
        else:
            print('Opção inválida, por favor digite SIM ou NÃO')

print('Programa finalizado!')
