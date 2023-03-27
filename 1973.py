N = int(input())
V = [int(x) for x in input().split()]
ESTRELAS = V
ATACADA = [False] * N
CARNEIROS = 0
for item in ESTRELAS:
    CARNEIROS += item

i = 0
ATAQUE = 0
ROUBOU = False
while i >= 0 and i < N:
    if ESTRELAS[i] > 0:
        ESTRELAS[i] -= 1
        CARNEIROS -= 1
        if not ATACADA[i]:
            ATACADA[i] = True
            ATAQUE += 1
        ROUBOU = True
    Q = ESTRELAS[i]
    if ROUBOU:
        Q += 1
        ROUBOU = False
    if Q % 2 == 0:
        i -= 1
    else:
        i += 1

print("{0} {1}".format(ATAQUE,CARNEIROS))