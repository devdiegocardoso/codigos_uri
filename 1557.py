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
        C = 1
        for i in range(0,N):
            AUX = C
            for j in range(0,N):
                M[i][j] = AUX
                AUX *= 2
            C *= 2
        TAM = len(str(M[N-1][N-1]))
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print("{0:{1}d}".format(M[i][j],TAM))
                else:
                    print("{0:{1}d} ".format(M[i][j],TAM),end="")
        print()

