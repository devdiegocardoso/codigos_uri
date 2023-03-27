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

N, G = in_list_int()
runas = {}
for _ in range(N):
    runa, valor = in_list_str()
    runas[runa] = int(valor)
X = in_int()
recitadas = in_list_str()

total = sum(runas[r] for r in recitadas if r in runas)
print_saida(f"{total}")
print_saida("You shall pass!" if total >= G else "My precioooous")