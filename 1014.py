def consumo(km,l):
    return km/l

KM = int(input())
L = float(input())

print("{:0.3f} km/l".format(consumo(KM,L)))
