
while True:
    try:
        N, M = [int(x) for x in input().split()]

        CITY = [0] * N

        for i in range(N):
            CITY[i] = [int(item) for item in input().split()]

        ponto1 = None
        ponto2 = None
        for i in range(N):
            for j in range(M):
                if CITY[i][j] == 1:
                    ponto1 = i,j
                if CITY[i][j] == 2:
                    ponto2 = i,j
        d = abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])
        print(d)
    except EOFError:
        break