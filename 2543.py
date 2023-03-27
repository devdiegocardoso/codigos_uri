while True:
    try:
        N, I = [int(x) for x in input().split()]
        C = 0
        for i in range(N):
            ID, JOGO =  [int(x) for x in input().split()]
            if ID == I and JOGO == 0:
                C += 1
        print(C)
    except EOFError:
        break
