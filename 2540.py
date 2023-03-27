while True:
    try:
        N = int(input())
        VOTOS = [int(x) for x in input().split()]
        C = sum(VOTOS)
        if C >= N * 2/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break  