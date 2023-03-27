N = int(input())

for i in range(N):
    vet = input().split(" ")
    X = int(vet[0])
    Y = int(vet[1])
    if Y != 0:
        print("{:.1f}".format(X/Y))
    else:
        print("divisao impossivel")
