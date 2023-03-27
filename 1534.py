lista = []
N = 0
while True:
    try:
        N = input()
        lista.append(int(N))
    except EOFError:
        break
    
for N in lista:
    M = [0] * N
    for i in range(N):
        M[i] = [0] * N
    for i in range(N):
        for j in range(N):
            if i <= j:
                if i + j == N - 1:
                    M[i][j] = 2
                    M[j][i] = 2
                elif i == j:
                    M[i][j] = 1
                    M[j][i] = 1
                else:
                    M[i][j] = 3
                    M[j][i] = 3
    for i in range(N):
        for j in range(N):
            print(M[i][j],end="")
        print()
