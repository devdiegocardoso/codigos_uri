while True:
    try:
        PAINEL = input()
        N = int(input())
        SINAIS = [int(x) for x in input().split()]
        MENSAGEM = ""
        for i in range(N):
            MENSAGEM += PAINEL[SINAIS[i]-1]
        print(MENSAGEM)
    except EOFError:
        break