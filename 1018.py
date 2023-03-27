notas = [100,50,20,10,5,2,1]
qtde = [0] * 7
def cedulas(V):
    for i,nota in enumerate(notas):
        qtde[i] = V // nota
        V = V % nota

valor = int(input())
cedulas(valor)
print(valor)
for i, data in enumerate(qtde):
    print("{0} nota(s) de R$ {1},00".format(data,notas[i]))
