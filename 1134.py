encerrado = False
A = 0
G = 0
D = 0
while not encerrado:
    opt = int(input())
    if opt == 1:
        A += 1
    elif opt == 2:
        G += 1
    elif opt == 3:
        D += 1
    elif opt == 4:
        encerrado = True

print("MUITO OBRIGADO")
print("Alcool: {}".format(A))
print("Gasolina: {}".format(G))
print("Diesel: {}".format(D))
