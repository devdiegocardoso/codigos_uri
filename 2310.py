N = int(input())

TSAQUE = 0
TBLOCK = 0
TATAQUE = 0

TSE = 0
TBE = 0
TAE = 0
for i in range(N):
    Nome = input()
    X, Y, Z = [int(x) for x in input().split()]
    Xl, Yl, Zl = [int(x) for x in input().split()]
    TSAQUE += X
    TBLOCK += Y
    TATAQUE += Z
    TSE += Xl
    TBE += Yl
    TAE += Zl

print("Pontos de Saque: {:.2f} %.".format(TSE/TSAQUE*100))
print("Pontos de Bloqueio: {:.2f} %.".format(TBE/TBLOCK*100))
print("Pontos de Ataque: {:.2f} %.".format(TAE/TATAQUE*100))