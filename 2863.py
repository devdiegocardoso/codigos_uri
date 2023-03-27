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

resultados = []
while 1:
    x = in_int()
    if not x:
        break
    tempos = [in_double() for _ in range(x)]
    resultados.append(min(tempos))

sys.stdout.write("\n".join(map(str,resultados)))
print()