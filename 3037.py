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

n_cases = in_int()

results = []
for _ in range(n_cases):
    p_maria = []
    p_joao = []
    for i in range(1,7):
        if i < 4:
            p_joao.append(in_list_int())
        else:
            p_maria.append(in_list_int())
    r_joao = sum(map(lambda x: x[0] * x[1],p_joao))
    r_maria = sum(map(lambda x: x[0] * x[1],p_maria))
    results.append("JOAO" if r_joao > r_maria else "MARIA")

sys.stdout.write('\n'.join(map(str,results)))