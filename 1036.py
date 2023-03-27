import math
def bhaskara(A,B,C):
    if A > 0:
        delta = (B*B) - (4 * A * C)
        #delta = round(delta,0)
        if delta > 0:
            x1 = (-B + math.sqrt(delta))/ (2 * A)
            x2 = (-B - math.sqrt(delta))/ (2 * A)
            print("R1 = {:0.5f}".format(x1))
            print("R2 = {:0.5f}".format(x2))
        else:
            print("Impossivel calcular")
    else:
        print("Impossivel calcular")

I = input().split()
A = float(I[0])
B = float(I[1])
C = float(I[2])

bhaskara(A,B,C)
