import math
encerrar = False
lista_leituras = []
while not encerrar:
    N = int(input())
    if N > 0:
        lista_leituras.append(N)
    else:
        encerrar = True

for N in lista_leituras:
    L = math.ceil(N/2)
    B = N
    if N > 0:
        M = [0] * N
        for i in range(N):
            M[i] = [0] * N
        for nivel in range(0,L):
            for i in range(nivel,B):
                for j in range(nivel,B):
                    M[i][j] = nivel+1
            B -= 1
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print("{0:3d}".format(M[i][j]))
                else:
                    print("{0:3d} ".format(M[i][j]),end="")
        print()

