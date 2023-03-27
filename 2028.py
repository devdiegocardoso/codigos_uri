def SOMA(N):
    if N == 0:
        return 1
    return SOMA(N-1) + N

def SEQ(N,C):
    Q = SOMA(N)
    STR = ''
    if N == 0:
        print("Caso {0}: {1} numero".format(C,Q))
    else:
        print("Caso {0}: {1} numeros".format(C,Q))
    for i in range(0,N + 1):
        if i == 0:
            STR += "{} ".format(i) * 1
        else:
            STR += "{} ".format(i) * i 
    print(STR.strip())
i = 1

SEQUENCIA = []

while True:
    try:
        S = int(input())
        SEQUENCIA.append(S)
    except EOFError:
        break

for S in SEQUENCIA:
    SEQ(S,i)
    print()
    i += 1
