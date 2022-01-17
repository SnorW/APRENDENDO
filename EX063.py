num1 = int(input('Digite um valor'))
loop = 0
numatual = num1
numanterior = 0

while loop <= 10:
    print(numatual)
    numatual += numanterior
    numanterior = numatual
    loop += 1
