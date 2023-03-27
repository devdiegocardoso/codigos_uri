V = [0] * 100
X = float(input())
V[0] = X

for i in range(1,len(V)):
    V[i] = V[i-1] / 2


for i in range(len(V)):
    print("N[{0}] = {1:.4f}".format(i,V[i]))
