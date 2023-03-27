N = int(input())
S = ""
for i in range(N):
    ANO = int(input())
    D = 2015 - ANO
    if D <= 0:
        S = "{} A.C.".format(abs(D)+1)
    else:
        S = "{} D.C.".format(abs(D))
    print(S)