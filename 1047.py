values = input()
string_v = values.split(" ")

HI = int(string_v[0])
MI = int(string_v[1])
HF = int(string_v[2])
MF = int(string_v[3])
H = 0
M = 0

if HI > HF:
    H = 24 - HI
    H = HF + H
    if MI > MF:
        H = H - 1
        M = 60 - MI
        M = MF + M
    else:
        M = MF - MI
elif HI < HF:
    H = HF - HI
    if MI > MF:
        H = H - 1
        M = 60 - MI
        M = MF + M
    else:
        M = MF - MI
else:
    H = 24
    if MI > MF:
        H = H - 1
        M = 60 - MI
        M = MF + M
    elif MI < MF:
        H = 0
        M = MF - MI

print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(H,M))
