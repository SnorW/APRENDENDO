n2 = 0
n3 = 0
for x in range(0, 6):
    n1 = int(input('Digite um numero'))
    if n1 % 2 != 1:
        n2 += n1
    elif n1 % 2 == 1:
        n3 += n1
print(n2)
print(n3)
