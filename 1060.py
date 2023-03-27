positivos = 0
for i in range(0,6):
    value = float(input())
    if value >= 0.0:
        positivos += 1

print("{0} valores positivos".format(positivos))
