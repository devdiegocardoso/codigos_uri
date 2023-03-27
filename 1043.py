values = input()

string_v = values.split(" ")
A = float(string_v[0])
B = float(string_v[1])
C = float(string_v[2])

if (abs(B - C) < A and A < B + C) and (abs(A - C) < B and B < A + C) and (abs(A - B) < C and C < A + B):
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((A + B) * C)/2
    print("Area = {:.1f}".format(area))
