N = int(input())

for i in range(N):
    p1 = input().strip()
    p2 = input().strip()
    if p1 == "ataque":
        if p2 == "pedra":
            print("Jogador 1 venceu")
        elif p2 == "papel":
            print("Jogador 1 venceu")
        else:
            print("Aniquilacao mutua")
    elif p1 == "papel":
        if p2 == "pedra":
            print("Jogador 2 venceu")
        elif p2 == "papel":
            print("Ambos venceram")
        else:
            print("Jogador 2 venceu")
    elif p1 == "pedra":
        if p2 == "pedra":
            print("Sem ganhador")
        elif p2 == "papel":
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")       