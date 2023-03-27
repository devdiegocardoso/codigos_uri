N = int(input())

for i in range(1,N+1):
    Q = i**2
    C = i**3
    print("{0} {1} {2}".format(i,Q,C))
    print("{0} {1} {2}".format(i,Q+1,C+1))
