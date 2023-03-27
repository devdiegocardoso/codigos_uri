lista = []
matriz = []
while True:
    try:
        N = input()
        lista.append(int(N))
        V = input().split(" ")
        for i in range(len(V)):
            V[i] = int(V[i])
        matriz.append(V)
    except EOFError:
        break
    except Exception:
        break

for i in range(len(lista)):
    maior = -1
    for j in range(lista[i]):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    if maior < 10:
        print(1)
    elif maior >= 10 and maior < 20:
        print(2)
    else:
        print(3)
