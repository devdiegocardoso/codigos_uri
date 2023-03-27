N = int(input())

for i in range(N):
    H,M,S = [int(x) for x in input().split()]
    if H < 10:
        H = "0"+str(H)
    if M < 10:
        M = "0"+str(M)
    if S == 1:
        print("{0}:{1} - A porta abriu!".format(H,M))
    else:
        print("{0}:{1} - A porta fechou!".format(H,M))