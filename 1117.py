valida = False
soma = 0
notas = 0
while not valida:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        soma += nota
        notas += 1
    else:
        print("nota invalida")
    if notas == 2:
        valida = True
media = soma / 2
print("media = {:.2f}".format(media))
