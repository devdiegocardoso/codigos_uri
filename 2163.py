N,M = [int(x) for x in input().split()]
MATRIZ = [0] * N
for i in range(N):
    MATRIZ[i] = [int(x) for x in input().split()]

filtro = [[7,7,7],[7,42,7],[7,7,7]]
lista = []
encontrou = False
for i in range(0,N-2):
    for j in range(0,M-2):
        lista.append(MATRIZ[i][j:j+3])
        lista.append(MATRIZ[i+1][j:j+3])
        lista.append(MATRIZ[i+2][j:j+3])
        if lista == filtro:
            print("{0} {1}".format(i+2,j+2))
            encontrou = True
            break
        lista.clear()
    if encontrou:
        break

if not encontrou:
    print("0 0")