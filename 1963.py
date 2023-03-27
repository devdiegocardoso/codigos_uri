A,B = input().split(" ")
A = float(A)
B = float(B)

D = B - A
P = D / A

print("{:.2f}%".format(P*100))