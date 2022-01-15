sal = float(input('Digite o salário'))

if sal > 1250.00:
    ssal = sal * 0.10
    print('Com o aumento de {:.2f} (10%) seu novo salário será: {:.2f} reais'.format(ssal, ssal + sal))
else:
    isal = sal * 0.15
    print('Com o aumento de {:.2f} (15%) seu novo salário será: {:.2f} reais'.format(isal, isal + sal))
