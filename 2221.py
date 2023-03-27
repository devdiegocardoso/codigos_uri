N = int(input())

for i in range(1,N+1):
    Bonus = int(input())
    Atx, Dfx, Lvx = [int(x) for x in input().split()]
    Aty, Dfy, Lvy = [int(x) for x in input().split()]
    
    if Lvx % 2 == 0:
        BonusX = Bonus
    else:
        BonusX = 0
    if Lvy % 2 == 0:
        BonusY = Bonus
    else:
        BonusY = 0
    VGx = ((Atx + Dfx) / 2) + BonusX
    VGy = ((Aty + Dfy) / 2) + BonusY

    if VGx > VGy:
        print("Dabriel")
    elif VGx < VGy:
        print("Guarte")
    else:
        print("Empate")
