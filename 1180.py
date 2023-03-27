N = int(input())
T = input().split(" ")
V = [0] * N
for i in range(len(V)):
    V[i] = int(T[i])    

menor = V[0]
posicao = 0
for i in range(1,N):
    if V[i] < menor:
        menor = V[i]
        posicao = i

print("Menor valor: {0}".format(menor))
print("Posicao: {0}".format(posicao))
