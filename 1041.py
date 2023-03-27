def coordenada(x,y):
    if x == 0 and y == 0:
        print("Origem")
    elif x == 0 and y != 0:
        print("Eixo Y")
    elif x != 0 and y == 0:
        print("Eixo X")
    elif x > 0 and y > 0:
        print("Q1")
    elif x > 0 and y < 0:
        print("Q4")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")

I = input().split()
x = float(I[0])
y = float(I[1])

coordenada(x,y)
