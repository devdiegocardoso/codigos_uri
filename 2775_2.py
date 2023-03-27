while True: 
    try: 
        N = int(input()) 
        L = input().split() 
        P = [] 
        for i in range(0, N, 1): 
            P.append(int(L[i])) 
        L = input().split() 
        T = [] 
        for i in range(0, N, 1): 
            T.append(int(L[i])) 
        tempo = 0 
        for _ in range(0, N - 1, 1): 
            a = 0 
            for i in range(0, N - 1, 1): 
                if P[i] > P[i + 1]: 
                    tempo += T[i] + T[i + 1] 
                    aux = P[i] 
                    P[i] = P[i + 1] 
                    P[i + 1] = aux
                    # aux = T[i]
                    # T[i] = T[i + 1]
                    # T[i + 1] = aux
                    a = 1
            if a == 0:
                break
        print(tempo)
    except EOFError: 
        break 
    