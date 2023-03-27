V = [0] * 20
for i in range(len(V)):
    N = int(input())
    V[i] = N
j = len(V)-1
for i in range(int(len(V)/2)):
    N = V[i]
    V[i] = V[j]
    V[j] = N
    j -= 1
for i in range(len(V)):
    print("N[{0}] = {1}".format(i,V[i]))
