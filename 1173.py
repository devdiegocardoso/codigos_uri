V = [0] * 10
N = int(input())
for i in range(10):
    V[i] = N
    N = N * 2

for i in range(10):
    print("N[{0}] = {1}".format(i,V[i]))
