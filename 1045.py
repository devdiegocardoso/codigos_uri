values = input()
string_v = values.split(" ")

A = float(string_v[0])
B = float(string_v[1])
C = float(string_v[2])

if A >= B + C or B >= A + C or C >= B + A:
    print("NAO FORMA TRIANGULO")
elif (A ** 2) == (B ** 2) + (C ** 2) or (B ** 2) == (C ** 2) + (A ** 2) or (C ** 2) == (B ** 2) + (A ** 2):
    print("TRIANGULO RETANGULO")
elif (A ** 2) > (B ** 2) + (C ** 2) or (B ** 2) > (C ** 2) + (A ** 2) or (C ** 2) > (B ** 2) + (A ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (A ** 2) < (B ** 2) + (C ** 2) or (B ** 2) < (C ** 2) + (A ** 2) or (C ** 2) < (B ** 2) + (A ** 2):
    print("TRIANGULO ACUTANGULO")

if A == B and B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")
