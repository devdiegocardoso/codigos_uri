while True:
    try:
        N, Q = [int(x) for x in input().split()]
        NOTAS = []

        for i in range(N):
            NOTAS.append(int(input()))
        NOTAS.sort(reverse=True)
        for i in range(Q):
            print(NOTAS[int(input())-1])
    except EOFError:
        break