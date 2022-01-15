nome = input('Digite seu nome')
nomesplit = nome.strip().split()
print("""Primeiro nome : {}
Último nome : {}""".format(nomesplit[0], nomesplit[len(nomesplit)-1]))
