
while True:
    try:
        T = int(input())

        NOTAS = 0
        CARGA = 0
        for i in range(T):
            N, C = [int(x) for x in input().split()]
            NOTAS += N * C
            CARGA += C
        IRA = NOTAS / (CARGA * 100)

        print("{:.4f}".format(IRA))
    except EOFError:
        break