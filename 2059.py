dados = [int(x) for x in input().split()]

par = True if dados[0] == 1 else False
soma = dados[1] + dados[2]
roubou = True if dados[3] == 1 else False
acusou = True if dados[4] == 1 else False

if soma % 2 == 0:
    if par and not roubou and not acusou:
        print("Jogador 1 ganha!")
    elif not par and not roubou and not acusou:
        print("Jogador 2 ganha!")
    else:
        if roubou and not acusou:
            print("Jogador 1 ganha!")
        elif roubou and acusou:
            print("Jogador 2 ganha!")
        elif not roubou and acusou:
            print("Jogador 1 ganha!")
else:
    if not par and not roubou and not acusou:
        print("Jogador 1 ganha!")
    elif par and not roubou and not acusou:
        print("Jogador 2 ganha!")
    else:
        if roubou and not acusou:
            print("Jogador 1 ganha!")
        elif roubou and acusou:
            print("Jogador 2 ganha!")
        elif not roubou and acusou:
            print("Jogador 1 ganha!")