S = 12
M = [0] * S
for i in range(S):
    M[i] = [0] * S

L = int(input())
T = input()

for i in range(0,S):
    for j in range(0,S):
        M[i][j] = float(input())
soma = 0
for i in range(0,S):
    soma += M[L][i]
if T == "M":
    print("{:.1f}".format(soma/S))
elif T == "S":
    print("{:.1f}".format(soma))
