N = int(input())

for i in range(1,N+1):
    if i % 2 == 0:
        print("{0}^{1} = {2}".format(i,2,i**2))
