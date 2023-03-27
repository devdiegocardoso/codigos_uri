N = int(input())
lista = [int(x) for x in input().split()]

multiplos = {2:0,3:0,4:0,5:0}
for i in range(N):
    C = lista[i]
    for multiplicador in multiplos.keys():
        if C % multiplicador == 0:
            multiplos[multiplicador] += 1

for multiplicador, qtde in multiplos.items():
    print("{0} Multiplo(s) de {1}".format(qtde,multiplicador))
