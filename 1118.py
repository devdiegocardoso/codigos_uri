valida = False
novo_calculo = True
soma = 0
notas = 0
while novo_calculo:
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
    opt = 3
    while opt != 1 and opt != 2:
        print("novo calculo (1-sim 2-nao)")
        opt = int(input())
        if opt == 1:
            valida = False
            notas = 0
            soma = 0
        elif opt == 2:
            novo_calculo = False
            
