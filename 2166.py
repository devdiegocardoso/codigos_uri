def base(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1/2
    return 1 / (2 + base(N-1))
 
N = int(input())

raiz = 1 + base(N)
print("{:.10f}".format(raiz))