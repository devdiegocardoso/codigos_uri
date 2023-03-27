notas = [2,5,10,20,50,100]
combinacoes = []

for i in range(len(notas)):
    for j in range(i,len(notas)):
        combinacoes.append(notas[i] + notas[j])

while True:
    N, M = [int(x) for x in input().split()]
    if M == 0 and N == 0:
        break
    else:
        TROCO = M - N
        combinou = False
        for combinacao in combinacoes:
            if combinacao == TROCO:
                combinou = True
                break
        if combinou:
            print("possible")
        else:
            print("impossible")
