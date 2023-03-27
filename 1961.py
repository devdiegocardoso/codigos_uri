V = input().split(" ")
PULO = int(V[0])
QTD_CANOS = int(V[1])

V = input().split(" ")
CANOS = [0] * QTD_CANOS
for i in range(QTD_CANOS):
    CANOS[i] = int(V[i])

venceu = True
for i in range(1,QTD_CANOS):
    D = CANOS[i] - CANOS[i-1]
    if abs(D) > PULO:
        venceu = False

if venceu:
    print("YOU WIN")
else:
    print("GAME OVER")