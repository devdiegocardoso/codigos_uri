def binet(N):
    F = ((((1 + (5 ** 0.5)) / 2) ** N) - ((((1 - (5 ** 0.5)) / 2)) ** N)) / (5 ** 0.5)
    return F

print("{:.1f}".format(binet(int(input()))))