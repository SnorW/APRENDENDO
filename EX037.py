n1 = int(input('Digite o valor para transformar'))
n2 = input("""Digite : 
[1] se quiser binário 
[2] se quiser octal  
[3] se quiser hexadecimal 
[4] se quiser todos os valores""")

if n2 == '1':
    print('O numero {} em binário é {}'.format(n1, bin(n1)[2:]))
elif n2 == '2':
    print('O numero {} em octal é {}'.format(n1, oct(n1)[2:]))
elif n2 == '3':
    print('O numero {} em hexadecimal é {}'.format(n1, hex(n1)[2:]))
elif n2 == '4':
    print('O numero {} em binário é "{}"'.format(n1, bin(n1)[2:]))
    print('O numero {} em octal é "{}"'.format(n1, oct(n1)[2:]))
    print('O numero {} em hexadecimal é "{}"'.format(n1, hex(n1)[2:]))
else:
    print('Digite entre [1] e [4]')
