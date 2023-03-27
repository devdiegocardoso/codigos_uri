A, B , C = [int(x) for x in input().split()]

if A >= B + C or B >= A + C or C >= A + B:
    print("Invalido")
else:
    if A == B and B == C:
        print("Valido-Equilatero")
    elif A == B or B == C or A == C:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    Aq = A * A
    Bq = B * B
    Cq = C * C
    if Aq == Bq + Cq or Bq == Aq + Cq or Cq == Aq + Bq:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
    