vet = input().split(" ")
M = int(vet[0])
N = int(vet[1])
while M >= 1 and N >= 1:
    somatorio = 0
    if M > N:
        tmp = M
        M = N
        N = tmp
    for i in range(M,N+1):
        print(i,end=" ")
        somatorio += i
    print("Sum={}".format(somatorio))
    vet = input().split(" ")
    M = int(vet[0])
    N = int(vet[1])
