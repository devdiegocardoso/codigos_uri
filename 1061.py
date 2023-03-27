linha = input().split(" ")
dia_inicio = int(linha[1])
linha = input().split(" : ")
hora_inicio = int(linha[0])
minuto_inicio = int(linha[1])
segundo_inicio = int(linha[2])

linha = input().split(" ")
dia_fim = int(linha[1])
linha = input().split(" : ")
hora_fim = int(linha[0])
minuto_fim = int(linha[1])
segundo_fim = int(linha[2])

dia = dia_fim - dia_inicio
hora = 0
minuto = 0
segundo = 0
if hora_inicio > hora_fim:
    dia -= 1
    hora = (24 - hora_inicio) + hora_fim
    if minuto_inicio > minuto_fim:
        hora -= 1
        minuto = (60 - minuto_inicio) + minuto_fim
        if segundo_inicio > segundo_fim:
            minuto -= 1
            segundo = (60 - segundo_inicio) + segundo_fim
        else:
            segundo = segundo_fim - segundo_inicio
    else:
        minuto = minuto_fim - minuto_inicio
        if segundo_inicio > segundo_fim:
            minuto -= 1
            segundo = (60 - segundo_inicio) + segundo_fim
        else:
            segundo = segundo_fim - segundo_inicio
else:
    hora = hora_fim - hora_inicio
    if minuto_inicio > minuto_fim:
        hora -= 1
        minuto = (60 - minuto_inicio) + minuto_fim
        if segundo_inicio > segundo_fim:
            minuto -= 1
            segundo = (60 - segundo_inicio) + segundo_fim
        else:
            segundo = segundo_fim - segundo_inicio
    else:
        minuto = minuto_fim - minuto_inicio
        if segundo_inicio > segundo_fim:
            minuto -= 1
            segundo = (60 - segundo_inicio) + segundo_fim
        else:
            segundo = segundo_fim - segundo_inicio
    

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))
