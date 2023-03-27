import math
L = []
while True:
    try:
        V = input().split()
        L.append(V)
    except EOFError:
        break

for item in L:
    V = item
    Xf = float(V[0]) 
    Yf = float(V[1])
    Xi = float(V[2])
    Yi = float(V[3])
    Vi = float(V[4])
    R1 = float(V[5])
    R2 = float(V[6])

    X = (Xi - Xf) ** 2
    Y = (Yi - Yf) ** 2

    D = math.sqrt(X + Y)
    D += Vi * 1.5

    R = R1 + R2
    
    if D > R:
        print("N")
    else:
        print("Y")