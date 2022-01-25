numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', "Seis", 'Sete', 'Oito', 'Nove', "Dez",
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

condicao_while = True
while condicao_while:
    user_intnumero = int(input('Digite um valor entre 0 e 20: '))

    if 0 <= user_intnumero <= len(numeros):
        print(numeros[user_intnumero])
        while True:
            tentar_nv = input('Deseja tentar novamente? S/N').strip().lower()
            if tentar_nv == 's' or tentar_nv == 'sim':
                break
            elif tentar_nv == 'n' or tentar_nv == 'não' or tentar_nv == 'nao':
                print('Programa finalizado, obrigado!')
                condicao_while = False
                break
            else:
                print('Por favor digite sim ou não')
    else:
        print('Opção inválida!')
