vet = input().split(" ")
X = int(vet[0])
Y = int(vet[1])
C = 1
for i in range(1,Y+1):
    if C == X:
        print("{}".format(i))
        C = 0
    else:
        print("{}".format(i),end=" ")
    C += 1
     
