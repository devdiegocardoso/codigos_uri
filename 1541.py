import math
encerrar =False

while not encerrar:
    V = input().split(" ")
    B = int(V[0])
    if B > 0:
        A = int(V[1])
        P = int(V[2])
        CASA = B * A
        TERRENO = (100 * CASA) / P
        print(int(math.sqrt(TERRENO)))
    else:
        encerrar = True
