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
    if N > 0:
        M = [0] * N
        for i in range(N):
            M[i] = [0] * N
        for i in range(0,N):
            C = 1
            for j in range(0,N):
                if i <= j:
                    M[i][j] = C
                    M[j][i] = M[i][j]
                    C += 1
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print("{0:3d}".format(M[i][j]))
                else:
                    print("{0:3d} ".format(M[i][j]),end="")
        print()

