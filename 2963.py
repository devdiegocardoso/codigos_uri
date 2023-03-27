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

def print_saida(texto):
    sys.stdout.write(f"{texto}\n")

N = in_int()

valores = [in_list_str() for _ in range(N)]
total_verba = sum(int(y) for x,y in valores if x == 'V')
total_gasto = sum(int(y) for x,y in valores if x == 'G')

print_saida("A greve vai parar." if total_gasto <= total_verba else "NAO VAI TER CORTE, VAI TER LUTA!")