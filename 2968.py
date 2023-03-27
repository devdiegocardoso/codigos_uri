import sys
from functools import cache
from math import ceil
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

voltas, placas = in_list_int()
total = voltas * placas

tempos = [ceil(total*(x/10)) for x in range(1,10)]

print_saida(" ".join(map(str,tempos)))

