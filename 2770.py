import sys

fastio = sys.stdin.readline
def in_int():
    return(int(fastio()))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_str():
    return(fastio().split())

resultados = []
while True:
    try:
        tmp = in_list_int()
        if not tmp:
            break
        x, y, p = tmp
        for i in range(p):
            xc, yc = in_list_int()
            if (xc <= x and yc <= y) or (yc <= x and xc <= y):
                resultados.append('Sim\n')
            else:
                resultados.append('Nao\n')
    except EOFError:
        break


sys.stdout.write("".join(map(str, resultados)))