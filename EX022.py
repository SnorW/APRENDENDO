import Cores

nomecompleto = input('Digite seu nome completo')
nomemai = nomecompleto.upper()
nomemin = nomecompleto.lower()
nomesplit = nomecompleto.split()
print('{}O nome {} em maiúsculas é {} e em minúsculas é {}'
      ' e possui {} letras sem espaço e o primeiro nome contém {} letras{}'
      .format(Cores.cores['vermelho'], nomecompleto, nomemai, nomemin, (len(nomecompleto) - 2), len(nomesplit[0]), Cores.cores['limpa']))
