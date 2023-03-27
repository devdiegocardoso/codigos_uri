encerrar = False
while not encerrar:
    X = int(input())
    if X != 0:
        for i in range(1,X+1):
            if i == X:
                print("{}".format(i))
            else:
                print("{}".format(i),end=" ")
    else:
        encerrar = True
