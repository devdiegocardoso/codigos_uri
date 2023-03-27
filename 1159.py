encerrar = False
soma = 0
while not encerrar:
    X = int(input())
    if X != 0:
        C = 0
        while C < 5:
            if X % 2 == 0:
                soma += X
                C += 1
            X += 1
        print(soma)
        soma = 0
    else:
        encerrar = True
