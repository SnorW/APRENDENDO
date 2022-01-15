y = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        print(x)
        y += x
print(y)
