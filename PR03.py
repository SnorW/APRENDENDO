from random import sample

nums = input('Digite 6 numeros de 1 a 99').strip().split()
nums.sort()

sorteionum = sample(range(1, 99), 6)
sorteionum.sort()
sorteionumstr = [str(x) for x in sorteionum]



print('Os numeros sorteados foram {}'.format(', '.join(sorteionumstr)))
print('Os seus numeros foram {}'.format(', '.join(nums)))
if sorteionumstr == nums:
    print('Parabéns você ganhou na lotéria !!!')
if sorteionumstr != nums:
    print('Não foi dessa vez, mas sinto suas chances crescendo !!')
