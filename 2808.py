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

def convertePosicao(posicao):
    return ord(posicao[0])-96, int(posicao[1])

p_inicio, p_destino = in_list_str()
x_inicio, y_inicio = convertePosicao(p_inicio)
x_destino, y_destino = convertePosicao(p_destino)

dx, dy = 0, 0
dx = abs(x_inicio - x_destino)
dy = abs(y_inicio - y_destino)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print("VALIDO")
else:
    print("INVALIDO")