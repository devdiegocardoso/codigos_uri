V = input().split(" ")

A = int(V[0])
B = int(V[1])
C = int(V[2])
D = int(V[3])

if A < B + C and B < A + C and C < A + B:
    print("S")
elif D < B + C and B < D + C and C < D + B:
    print("S")
elif A < D + C and D < A + C and C < D + A:
    print("S")
elif A < B + D and B < A + D and D < A + B:
    print("S")
else:
    print("N") 