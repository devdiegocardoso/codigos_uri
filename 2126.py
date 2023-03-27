class Numeros:
    def __init__(self,N1,N2):
        self.N1 = N1
        self.N2 = N2
    def contar(self):
        count = start = 0
        while True:
            start = self.N2.find(self.N1, start) + 1
            if start > 0:
                count+=1
            else:
                break
        return count , self.N2.rfind(self.N1)+1

entradas = []

while True:
    try:
        N1 = input().strip()
        N2 = input().strip()
        entradas.append(Numeros(N1,N2))
    except EOFError:
        break
i = 1
for entrada in entradas:
    print("Caso #{}:".format(i))
    Q, P = entrada.contar()
    if Q == 0:
        print("Nao existe subsequencia")
    else:
        print("Qtd.Subsequencias:",Q)
        print("Pos:",P)
    print()
    i += 1