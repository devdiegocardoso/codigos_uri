def maior(A,B):
    return int((A+B+abs(A-B))/2)

entrada = input().split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])

print("{0} eh o maior".format(maior(maior(A,B),C)))
