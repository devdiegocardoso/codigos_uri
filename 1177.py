V = [0] * 1000
T = int(input())
j = 0
for i in range(len(V)):
    if j == T:
        j = 0
    V[i] = j
    j += 1

for i in range(len(V)):
    print("N[{0}] = {1}".format(i,V[i]))
