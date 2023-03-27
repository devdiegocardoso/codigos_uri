N = int(input())

PRODUTOS = {1001:1.50,1002:2.50,1003:3.50,1004:4.50,1005:5.50}
TOTAL = 0
for i in range(N):
    CODIGO, QTDE = [int(x) for x in input().split()]
    TOTAL += PRODUTOS[CODIGO] * QTDE

print("{:.2f}".format(TOTAL))