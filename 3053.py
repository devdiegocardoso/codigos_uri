import sys
from functools import cache

fastio = sys.stdin.readline
def in_int():
    x = fastio()
    if not x:
        return None
    return(int(x))
def in_double():
    x = fastio()
    if not x:
        return None
    return(float(x))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_double():
    return(list(map(float,fastio().split())))
def in_list_str():
    return(fastio().split())
def in_str():
    x = fastio()
    if not x:
        return None
    return x.replace('\n','')

n_movimentos = in_int()
posicao_inicial = in_str()
results = []
dict_inicio = {'A':0,'B':1,'C':2}
dict_fim = {0:'A',1:'B',2:'C'}
mesa = [0,0,0]
mesa[dict_inicio[posicao_inicial]] = 1
sequencia = [in_int() for _ in range(n_movimentos)]

for movimento in sequencia:
    if movimento == 1:
        mesa[0], mesa[1] = mesa[1], mesa[0]
    elif movimento == 2:
        mesa[1], mesa[2] = mesa[2], mesa[1]
    elif movimento == 3:
        mesa[0], mesa[2] = mesa[2], mesa[0]

sys.stdout.write(f'{dict_fim[mesa.index(1)]}\n')
