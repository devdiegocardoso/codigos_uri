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

N,C,M = in_list_int()
carimbadas = in_list_int()
figurinhas = {x for x in in_list_int()}

resultado = sum(figurinha not in figurinhas for figurinha in carimbadas)
print(resultado)
