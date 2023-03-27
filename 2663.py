N_COMPETIDORES = int(input())
MIN_CLASSIFICADOS = int(input())
COMPETIDORES = []
for i in range(0,N_COMPETIDORES):
    COMPETIDORES.append(int(input()))

total_classificados = 0

COMPETIDORES.sort(reverse=True)
for i in range(total_classificados,N_COMPETIDORES):
    atual = COMPETIDORES[total_classificados]
    total_classificados += 1
    while total_classificados < len(COMPETIDORES):
        if COMPETIDORES[total_classificados] != atual:
            break
        total_classificados += 1
    if total_classificados >= MIN_CLASSIFICADOS:
        break

print(total_classificados)
