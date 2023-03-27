T = int(input())

tabela = {"sucodelaranja":120,"morangofresco":85,"mamao":85,"goiabavermelha":70,"manga":56,"laranja":50,"brocolis":34}

MIN = 110
MAX = 130

while T != 0:
    T_GRAMAS = 0
    for i in range(T):
        LISTA = input().split()
        QTDE = int(LISTA[0])
        ALIMENTO = ''
        for i in range(1,len(LISTA[1:])+1):
            ALIMENTO += LISTA[i]
        T_GRAMAS += QTDE * tabela[ALIMENTO]
    if T_GRAMAS >= MIN and T_GRAMAS <= MAX:
        print("{} mg".format(T_GRAMAS))
    elif T_GRAMAS < MIN:
        print("Mais {} mg".format(MIN-T_GRAMAS))
    else:
        print("Menos {} mg".format(T_GRAMAS-MAX))

    T = int(input())