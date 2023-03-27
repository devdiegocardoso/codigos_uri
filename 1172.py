V = [0] * 10
for i in range(10):
    N = int(input())
    if N <= 0:
        V[i] = 1
    else:
        V[i] = N

for i in range(10):
    print("X[{0}] = {1}".format(i,V[i]))
