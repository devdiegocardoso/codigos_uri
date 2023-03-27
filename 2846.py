import sys
from functools import cache

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
def in_str():
    x = fastio()
    if not x:
        return None
    return x.replace('\n','')


resultados = []
while 1:
    x = in_str()
    if not x:
        break
    if x == 'esquerda':
        resultados.append('ingles')
    elif x == 'direita':
        resultados.append('frances')
    elif x == 'nenhuma':
        resultados.append('portugues')
    else:
        resultados.append('caiu')
    
sys.stdout.write("\n".join(resultados))
print()