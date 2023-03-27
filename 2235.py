C1, C2, C3 = [int(x) for x in input().split()]

ANO = 2016
achou = False
comb = [ANO+C1,ANO-C1,ANO+C2,ANO-C2,ANO+C3,ANO-C3,ANO+C1+C2,ANO+C1+C3,ANO+C1-C2,ANO+C1-C3,ANO-C1+C2,ANO-C1+C3,ANO-C1-C2,ANO-C1-C3,ANO+C2+C3,ANO+C2-C3,ANO-C2-C3,ANO-C2+C3,ANO+C1+C2+C3,ANO+C1+C2-C3,ANO+C1-C2-C3,ANO-C1-C2-C3,ANO-C1+C2+C3,ANO-C1-C2+C3,ANO+C1-C2+C3,ANO-C1+C2-C3]

for item in comb:
    if item == ANO:
        achou = True
        break

if achou:
    print('S')
else:
    print('N')


