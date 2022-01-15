import random
from emoji import emojize
vn = int(input('Digite um numero'))
vr = random.randint(0, 5)
if vn == vr:
    print(emojize(':fireworks::moneybag: Você Ganhou :fireworks::moneybag:', use_aliases=True))
else:
    print(emojize(':sob: Infelizmente não foi dessa vez , tente novamente! :sob:', use_aliases=True))
print('O numero sorteado foi {}'.format(vr))
