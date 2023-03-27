V = [0] * 100

for i in range(len(V)):
    N = float(input())
    V[i] = N

for i in range(len(V)):
    if V[i] <= 10:
        print("A[{0}] = {1}".format(i,V[i]))
