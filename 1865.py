N = int(input())

for i in range(N):
    V = input().split(" ")
    nome = V[0]
    newtons = int(V[1])
    if nome == "Thor":
        print("Y")
    else:
        print("N")
