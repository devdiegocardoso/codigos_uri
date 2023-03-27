N = int(input())
for i in range(N):
    V = int(input())
    primo = True
    for j in range(2,V):
        if V % j == 0:
            primo = False
            break
    if not primo:
        print("{} nao eh primo".format(V))
    else:
        print("{} eh primo".format(V))
