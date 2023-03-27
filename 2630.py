N = int(input())

def converter(tipo,vetor):
    if tipo == 'min':
        return min(vetor)
    elif tipo == 'max':
        return max(vetor)
    elif tipo == 'mean':
        return int(sum(vetor)/len(vetor))
    else:
        return int(0.3*vetor[0]+0.59*vetor[1]+0.11*vetor[2])

for i in range(1,N+1):
    tipo = input()
    RGB = [int(x) for x in input().split()]
    print("Caso #{0}: {1}".format(i,converter(tipo,RGB)))
