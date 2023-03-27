n_casos = int(input())

results = []
for _ in range(n_casos):
    filtros = [int(x) for x in input().split()]
    aparelhos = sum(filtros[1:]) - len(filtros[1:]) + 1
    results.append(aparelhos)

for result in results:
    print(result)