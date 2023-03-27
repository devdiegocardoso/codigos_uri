N = int(input())
C = 0
R = 0
S = 0
T = 0
for i in range(N):
    vet = input()
    cobaias, tipo = vet.split(" ")
    cobaias = int(cobaias)
    T += cobaias
    if tipo == "C":
        C += cobaias
    elif tipo == "R":
        R += cobaias
    else:
        S += cobaias

print("Total: {} cobaias".format(T))
print("Total de coelhos: {}".format(C))
print("Total de ratos: {}".format(R))
print("Total de sapos: {}".format(S))
PC = (C / T) * 100
PR = (R / T) * 100
PS = (S / T) * 100
print("Percentual de coelhos: {:.2f} %".format(PC))
print("Percentual de ratos: {:.2f} %".format(PR))
print("Percentual de sapos: {:.2f} %".format(PS))
