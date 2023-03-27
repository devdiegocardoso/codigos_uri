T = int(input())

fib = [0] * 61
fib[1] = 1
for i in range(2,len(fib)):
    fib[i] = fib[i-1]+fib[i-2]

for i in range(T):
    N = int(input())
    F = fib[N]
    print("Fib({0}) = {1}".format(N,F))
