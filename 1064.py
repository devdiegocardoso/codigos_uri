positivos = 0
somatorio = 0
for i in range(0,6):
    value = float(input())
    if value >= 0.0:
        positivos += 1
        somatorio += value

media = somatorio / positivos

print("{0} valores positivos".format(positivos))
print("{:0.1f}".format(media))
