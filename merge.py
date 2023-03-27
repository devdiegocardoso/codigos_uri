def mesclar(v1,v2):
    c = []
    while v1 and v2:
        if v1[0] > v2[0]:
            c.append(v2[0])
            v2.pop(0)
        else:
            c.append(v1[0])
            v1.pop(0)
    while v1:
        c.append(v1[0])
        v1.pop(0)
    while v2:
        c.append(v2[0])
        v2.pop(0)
    return c

def mergesort(vetor,indices):
    n = len(vetor)
    s = 0
    if n == 1:
        return vetor

    l1 = vetor[:n//2]
    l2 = vetor[n//2:]

    l1 = mergesort(l1)
    l2 = mergesort(l2)

    return mesclar(l1,l2)
