T = int(input())
for i in range(T):
    vet = input().split(" ")
    PA = int(vet[0])
    PB = int(vet[1])
    G1 = float(vet[2])
    G2 = float(vet[3])
    C1 = 0
    C2 = 0
    ANOS = 0
    while PA <= PB:
        C1 = int(PA * (G1/100))
        C2 = int(PB * (G2/100))
        PA += C1
        PB += C2
        ANOS += 1
        if ANOS > 100:
            break
    if ANOS <= 100:
        print("{} anos.".format(ANOS))
    else:
        print("Mais de 1 seculo.")
