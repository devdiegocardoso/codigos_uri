encerrar = False
soma = 0
Q = 0
while not encerrar:
    I = int(input())
    if I < 0:
        encerrar = True
    else:
        soma += I
        Q += 1

if Q > 0:
    print("{:.2f}".format(soma/Q))
