QT = int(input())

for i in range(QT):
    jogadas = input().split(" ")
    valores = input().split(" ")
    P1 = int(valores[0])
    P2 = int(valores[1])
    P1Nome = jogadas[0]
    P2Nome = jogadas[2]
    P1Escolha = jogadas[1]
    P2Escolha = jogadas[3]

    if (P1 + P2) % 2 == 0:
        if P1Escolha == "PAR":
            print(P1Nome)
        else:
            print(P2Nome)
    else:
        if P1Escolha == "IMPAR":
            print(P1Nome)
        else:
            print(P2Nome)