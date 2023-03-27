M, XP = [int(x) for x in input().split()]

while True:
    if M == 0 and XP == 0:
        break
    V = M * XP
    print(V)
    M, XP = [int(x) for x in input().split()]