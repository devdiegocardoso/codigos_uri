import sys

fastio = sys.stdin.readline
def in_int():
    x = fastio()
    if not x:
        return None
    return(int(x))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_double():
    return(list(map(float,fastio().split())))
def in_list_str():
    return(fastio().split())

casos = in_int()
resultados = []
for _ in range(casos):
    tam = in_int()
    lista = in_list_int()
    impares = [x for x in lista if x % 2 != 0]
    ordenados = []
    while impares:
        removido = False
        maior = max(impares)
        menor = min(impares)
        if impares:
            impares.remove(maior)
        if impares:
            removido = True
            impares.remove(menor)
        ordenados.extend([maior,menor] if removido else [maior])
    resultados.append(ordenados)

mapped = [" ".join(map(str,item)) for item in resultados]
sys.stdout.write("\n".join(mapped))
print()