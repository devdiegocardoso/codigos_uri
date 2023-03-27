qtde = int(input())

horas_boneco = 8
horas_arquiteto = 4
horas_musico = 6
horas_desenhista = 12

acumulado_boneco = 0
acumulado_arquiteto = 0
acumulado_musico = 0
acumulado_desenhista = 0

total_presentes = 0
for _ in range(qtde):
    _, grupo, horas = input().split()
    if grupo == 'bonecos':
        acumulado_boneco += int(horas)
    elif grupo == 'arquitetos':
        acumulado_arquiteto += int(horas)
    elif grupo == 'musicos':
        acumulado_musico += int(horas)
    elif grupo == 'desenhistas':
        acumulado_desenhista += int(horas)

resultado = sum([acumulado_boneco // horas_boneco, acumulado_arquiteto // horas_arquiteto, acumulado_musico // horas_musico, acumulado_desenhista // horas_desenhista])
print(resultado)