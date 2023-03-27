maior = -1
posicao = 0
for i in range(1,101):
    N = int(input())
    if N > maior:
        maior = N
        posicao = i

print(maior)
print(posicao)
