
while True:
    try:
        N, AMIN, AMAX = [int(x) for x in input().split()]
        C = 0
        for i in range(N):
            A = int(input())
            if A >= AMIN and A <= AMAX:
                C += 1
        print(C)
    except EOFError:
        break

        
