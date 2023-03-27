novo_jogo = True
INTER = 0
GREMIO = 0
EMPATE = 0
VENCEDOR = 0
JOGOS = 0
while novo_jogo:
    vet = input().split(" ")
    P1 = int(vet[0])
    P2 = int(vet[1])
    JOGOS += 1
    if P1 > P2:
        INTER += 1
    elif P2 > P1:
        GREMIO += 1
    else:
        EMPATE += 1
    opt = -1
    while opt != 1 and opt != 2:
        opt = int(input("Novo grenal (1-sim 2-nao)\n"))
        if opt == 2:
            novo_jogo = False

print("{} grenais".format(JOGOS))
print("Inter:{}".format(INTER))
print("Gremio:{}".format(GREMIO))
print("Empates:{}".format(EMPATE))
if GREMIO > INTER:
    print("Gremio venceu mais")
elif GREMIO < INTER:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
