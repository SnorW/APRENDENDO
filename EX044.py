valor = int(input('Qual o valor total das compras?'))
formapag = int(input("""Escolha a forma de pagamento 
[1] á vista dinheiro/cheque/pix/boleto
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão"""))

avistadin = valor - (valor * 0.10)
avistacart = valor - (valor * 0.05)
duasvezescart = valor
tresoumais = valor + (valor * 0.20)

if formapag == 1:
    print('O preço final a se pagar é de R${:.2f}'.format(avistadin))
elif formapag == 2:
    print('O preço final a se pagar é de R${:.2f}'.format(avistacart))
elif formapag == 3:
    print('O preço final a se pagar é de R${:.2f}'.format(duasvezescart))
    print('Com parcelas de R${}'.format(duasvezescart / 2))
elif formapag == 4:
    parcela = int(input('Em quantas vezes irá parcelar?'))
    if parcela > 2:
        print('O preço final a se pagar é de R${:.2f}'.format(tresoumais))
        print('Com parcelas de R${:.2f}'.format(tresoumais / parcela))
    else:
        print('O preço final a se pagar é de R${:.2f}'.format(duasvezescart))
        print('Com parcelas de R${}'.format(duasvezescart / 2))
else:
    print('Opção inválida , tente novamente!')
