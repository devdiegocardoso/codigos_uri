X = int(input())
encerrar = False
while not encerrar:
    Z = int(input())
    if Z > X:
        encerrar = True
C = 0
soma = 0

while soma < Z:
    soma += X
    X += 1
    C += 1

print(C)
