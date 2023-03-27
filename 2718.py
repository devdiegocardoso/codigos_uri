def verificaSequencia(seq):
    agrupamento = [len(x) for x in bin(seq)[2:].split('0')]
    return max(agrupamento)

grupos = int(input())

lista = []
for i in range(grupos):
    grupo = int(input())
    #print(verificaSequencia(grupo))
    lista.append(verificaSequencia(grupo))

print(*lista,sep='\n')