N = int(input())

resultados = []

for i in range(N):
    myDict = {}
    Nome = input()
    Dificuldade = float(input())
    Notas = [float(x) for x in input().split()]
    Menor = min(range(len(Notas)),key=Notas.__getitem__)
    del Notas[Menor]
    Maior = max(range(len(Notas)),key=Notas.__getitem__)
    del Notas[Maior]
    Total = sum(Notas)
    myDict[Nome] = Total * Dificuldade
    resultados.append(myDict)

for item in resultados:
    for key, value in item.items():
        print("{0} {1:.2f}".format(key,value))


