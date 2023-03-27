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


qtde = in_int()
qtde_raca = [0] * 5
racas = {'X':0,'H':1,'E':2,'A':3,'M':4}
for _ in range(qtde):
    nome, raca = in_list_str()
    qtde_raca[racas.get(raca)] += 1

print_saida(f"{qtde_raca[0]} Hobbit(s)")
print_saida(f"{qtde_raca[1]} Humano(s)")
print_saida(f"{qtde_raca[2]} Elfo(s)")
print_saida(f"{qtde_raca[3]} Anao(s)")
print_saida(f"{qtde_raca[4]} Mago(s)")