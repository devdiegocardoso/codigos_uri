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

N = in_int()
seq = in_list_int()

escadinhas = 1
i = 2
if N > 2:
    diferenca = seq[0] - seq[1] 
    while i < N:
        if seq[i-1] - seq[i] == diferenca:
            i += 1
        else:
            diferenca = seq[i-1] - seq[i]
            escadinhas += 1
    print(escadinhas)
else:
    print(1)

