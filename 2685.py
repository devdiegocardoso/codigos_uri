angulos = []

while True:
    try:
        S = int(input())
        angulos.append(S)
    except EOFError:
        break

for angulo in angulos:
    if angulo >= 0 and angulo <= 89 or angulo == 360:
        print("Bom Dia!!")
    elif angulo >= 90  and angulo <= 179:
        print("Boa Tarde!!")
    elif angulo >= 180 and angulo <= 269:
        print("Boa Noite!!")
    else:
        print("De Madrugada!!")
