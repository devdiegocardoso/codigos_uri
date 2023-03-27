angulos = []

while True:
    try:
        S = float(input())
        angulos.append(S)
    except EOFError:
        break

segundos_dia = 24 * 60 * 60
for angulo in angulos:
    hora_quad = ((angulo+90) * segundos_dia) / 360
    horas = int(hora_quad // (60 * 60))
    minutos_quad = hora_quad % (60 * 60)
    minutos = int(minutos_quad // (60))
    segundos_quad = minutos_quad % 60
    segundos = int(segundos_quad)
    
    if angulo >= 0 and angulo <= 89.999999 or angulo == 360:
        print("Bom Dia!!")
    elif angulo >= 90  and angulo <= 179.999999:
        print("Boa Tarde!!")
    elif angulo >= 180 and angulo <= 269.999999:
        print("Boa Noite!!")
    else:
        print("De Madrugada!!")
    print(f"{horas-24 if horas > 23 else horas:02}:{minutos:02}:{segundos:02}")
