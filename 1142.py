N = int(input())
C = 1
for i in range(1,N+1):
    for j in range(1,5):
        if j == 4:
            print("PUM")
        else:
            print("{}".format(C),end=" ")
        C += 1
