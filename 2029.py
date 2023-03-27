class Produtor:
    def __init__(self,VOLUME,DIAMETRO):
        self.VOLUME = VOLUME
        self.DIAMETRO = DIAMETRO

PI = 3.14
produtores = []
while True:
    try:
        MEL = float(input())
        D = float(input())
        produtores.append(Produtor(MEL,D))
    except EOFError:
        break

for produtor in produtores:
    RAIO = produtor.DIAMETRO / 2 
    B = PI * (RAIO ** 2)
    A = produtor.VOLUME / B
    print("ALTURA = {:.2f}".format(A))
    print("AREA = {:.2f}".format(B))
    
