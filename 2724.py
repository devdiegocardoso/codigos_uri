import re

def verificaSublista(lista,sub):
    tam_lista = len(lista)
    tam_sub = len(sub)
    limit = tam_lista-tam_sub+1
    if limit < 1:
        return False
    for i in range(limit):
        c = 0
        for j in range(tam_sub):
            if lista[i+j] == sub[j]:
                c += 1
        if c == tam_sub:
            return True
    return False

def verificaExperimentos(compostos,experimentos):
    resultados = ''
    for experimento in experimentos:
        achou_perigoso = False
        for composto in compostos:
            elementos_experimento = re.findall("[A-Z]{1}[a-z]?[0-9]*",experimento)
            elementos_composto = re.findall("[A-Z]{1}[a-z]?[0-9]*",composto)
            if verificaSublista(elementos_experimento,elementos_composto):
                achou_perigoso = True
                break
        resultados += 'Abortar\n' if achou_perigoso else 'Prossiga\n'
    return resultados

casos = int(input())
resultados = []
for i in range(casos):
    compostos = []
    experimentos = []
    n_compostos = int(input())
    for j in range(n_compostos):
        compostos.append(input())
    n_experimentos = int(input())
    for j in range(n_experimentos):
        experimentos.append(input())
    resultados.append(verificaExperimentos(compostos,experimentos))

for i in range(len(resultados)):
    print(resultados[i] if i < len(resultados) -1 else resultados[i][:-1])
