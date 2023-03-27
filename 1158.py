N = int(input())

for i in range(N):
    vet = input().split(" ")
    X = int(vet[0])
    Y = int(vet[1])
    C = 0
    soma = 0
    while C < Y:
        if X % 2 != 0:
            C += 1
            soma += X
        X += 1
    print(soma)
