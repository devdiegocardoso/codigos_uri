N = int(input())
for i in range(N):
    V = int(input())
    S = 0
    for i in range(1,V):
        if V % i == 0:
            S += i
    if S == V:
        print("{} eh perfeito".format(V))
    else:
        print("{} nao eh perfeito".format(V))
