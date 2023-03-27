while True:
    try:
        N = int(input())
        dias = [1]
        T, D = [int(x) for x in input().split()]
        melhor = T / D
        for i in range(2,N+1):
            T, D = [int(x) for x in input().split()]
            if T / D < melhor:
                dias.append(i)
                melhor = T / D
        for elem in dias:
            print(elem)
    except EOFError:
        break