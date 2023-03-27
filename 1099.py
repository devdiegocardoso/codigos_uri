N = int(input())

for i in range(N):
    vet = input()
    X,Y = vet.split(" ")
    X = int(X)
    Y = int(Y)
    if X > Y:
        tmp = X
        X = Y
        Y = tmp
    somatorio = 0
    for j in range(X+1,Y):
        if j % 2 != 0:
            somatorio += j
    print(somatorio)
