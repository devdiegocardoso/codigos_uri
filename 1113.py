vet = input().split(" ")
M = int(vet[0])
N = int(vet[1])
while M != N:
    if M < N:
        print("Crescente")
    else:
        print("Decrescente")
    vet = input().split(" ")
    M = int(vet[0])
    N = int(vet[1])
