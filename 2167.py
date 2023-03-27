N = int(input())
ROTACOES = [int(x) for x in input().split()]

indice = 0
for i in range(1,N):
    if ROTACOES[i-1] > ROTACOES[i]:
        indice = i+1
        break

print(indice)