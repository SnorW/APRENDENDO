distancia = float(input('Qual a distância em quilômetros?'))
if distancia <= 200:
    print('O valor da passagem para {:.3f} quilômetros é R${:.2f}'.format(distancia, distancia * 0.5))
else:
    print('O valor da passagem para {:.3f} quilômetros é R${:.2f}'.format(distancia, distancia * 0.45))
