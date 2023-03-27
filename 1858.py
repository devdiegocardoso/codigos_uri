N = int(input())
P = input().split(" ")

for i in range(N):
    P[i] = int(P[i])

menor = P[0]
pessoa = 1
for i in range(1,N):
    if P[i] < menor:
        pessoa = i + 1
        menor = P[i]

print(pessoa)
