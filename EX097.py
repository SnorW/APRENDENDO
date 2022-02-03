def escreva(txt):
    formato_traco = len(txt) * 2
    formato_parametro = len(txt) // 2
    print('-'*formato_traco)
    print(' '*formato_parametro, f'{txt:}')
    print('-'*formato_traco)


escreva('Olá mundo')
escreva('Partiu américa')