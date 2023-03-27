N = int(input())
paisagem = [int(x) for x in input().split()]
pico = False
vale = False
anterior = ""
atual = ""
padrao = True
for i in range(N-1):
    anterior = atual
    if paisagem[i] < paisagem[i+1]:
        atual = "vale"
    elif paisagem[i] > paisagem[i+1]:
        atual = "pico"
    if anterior == atual:
        padrao = False
        break

if padrao:
    print(1)
else:
    print(0)
    