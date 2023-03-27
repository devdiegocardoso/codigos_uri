while True:
    try:
        N = int(input())
        C = 0
        while N // 2 != 0:
            C += 1
            N = N // 2
        print(C)
    except EOFError:
        break