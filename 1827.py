import math
lista = []
while True:
    try:
        N = input()
        lista.append(int(N))
    except EOFError:
        break
    except Exception:
        break

for N in lista:
    M = [0] * N
    for i in range(N):
        M[i] = [0] * N
    for i in range(int(N/3),N - int(N/3)):
        for j in range(int(N/3),N - int(N/3)):
            if i <= j:
                M[i][j] = 1
                M[j][i] = 1
    for i in range(N):
        for j in range(N):
            if i <= j and M[i][j] != 1:
                if i == j:
                    M[i][j] = 2
                    M[j][i] = 2
                if i + j == N - 1 and M[i][j] != 4:
                    M[i][j] = 3
                    M[j][i] = 3
    M[int(N/2)][int(N/2)] = 4
    for i in range(N):
        for j in range(N):
            print("{}".format(M[i][j]),end="")
        print()
    print()
