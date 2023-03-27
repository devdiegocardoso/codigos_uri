while True:
    try:
        N = int(input())
        M, L = [int(x) for x in input().split()]
        B1 = []
        B2 = []
        for i in range(M):
            B1.append([int(x) for x in input().split()])
        for i in range(L):
            B2.append([int(x) for x in input().split()])
        C1, C2 = [int(x) for x in input().split()]
        ATRIBUTO = int(input())
        if B1[C1-1][ATRIBUTO-1] > B2[C2-1][ATRIBUTO-1]:
            print("Marcos")
        elif B1[C1-1][ATRIBUTO-1] < B2[C2-1][ATRIBUTO-1]:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break