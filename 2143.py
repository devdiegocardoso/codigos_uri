while True:
    T = int(input())
    if T == 0:
        break
    else:
        for i in range(T):
            P = int(input())
            if P % 2 == 0:
                V = (P * 2) - 2
                print(V)
            else:
                V = (P * 2) - 1
                print(V) 