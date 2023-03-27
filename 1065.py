positivos = 0
for i in range(0,5):
    value = int(input())
    if value % 2 == 0:
        positivos += 1

print("{0} valores pares".format(positivos))
