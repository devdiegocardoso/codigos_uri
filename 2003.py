MAXIMO = 60
LIMITE = 8 * 60
while True:
    try:
        HORA,MINUTO = [int(x) for x in input().split(":")]
        MINUTOS = (HORA * 60) + MINUTO + MAXIMO
        D = MINUTOS - LIMITE
        if D > 0:
            print("Atraso maximo:",D)
        else:
            print("Atraso maximo: 0")
    except EOFError:
        break

        