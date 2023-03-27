S = 12
M = [0] * S
for i in range(S):
    M[i] = [0] * S

T = input()

for i in range(0,S):
    for j in range(0,S):
        M[i][j] = float(input())
soma = 0
Q = 0
for i in range(0,S):
    for j in range(0,S):
        if i + j != S - 1 and i != j:
            if i > j and i + j >= S:
                soma += M[i][j]
                Q += 1
if T == "M":
    print("{:.1f}".format(soma/Q))
elif T == "S":
    print("{:.1f}".format(soma))
