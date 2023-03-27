vet = input().split(" ")
X = int(vet[0])
Y = int(vet[1])

while X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X < 0 and Y < 0:
        print("terceiro")
    else:
        print("quarto")
    vet = input().split(" ")
    X = int(vet[0])
    Y = int(vet[1])
