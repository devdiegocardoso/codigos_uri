N = int(input())
vet = []
CENTENA = (N//100)*100
DEZENA = ((N-CENTENA)//10)*10
UNIDADE = N - (DEZENA + CENTENA)
vet.append(CENTENA)
vet.append(DEZENA)
vet.append(UNIDADE)
ROMANO = ""
for valor in vet:
    if valor >= 100:
        if valor in range(100,400):
            V = valor // 100
            ROMANO += "C" * V
        elif valor in range(400,600):
                if valor == 400:
                    ROMANO += "CD"
                elif valor == 500:
                    ROMANO += "D"
        elif valor in range(600,900):
            ROMANO += "D"
            V = valor // 100
            ROMANO += "C" * (V - 5)
        elif valor == 900:
            ROMANO += "CM"
    elif valor >= 10:
        if valor in range(10,40):
            V = valor // 10
            ROMANO += "X" * V
        elif valor in range(40,60):
                if valor == 40:
                    ROMANO += "XL"
                elif valor == 50:
                    ROMANO += "L"
        elif valor in range(60,90):
            ROMANO += "L"
            V = valor // 10
            ROMANO += "X" * (V - 5)
        elif valor == 90:
            ROMANO += "XC"
    elif valor >= 1:
        if valor in range(1,4):
            V = valor // 1
            ROMANO += "I" * V
        elif valor in range(4,6):
                if valor == 4:
                    ROMANO += "IV"
                elif valor == 5:
                    ROMANO += "V"
        elif valor in range(6,9):
            ROMANO += "V"
            V = valor // 1
            ROMANO += "I" * (V - 5)
        elif valor == 9:
            ROMANO += "IX"
            
print(ROMANO)