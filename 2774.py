import sys

fastio = sys.stdin.readline
def in_int():
    return(int(fastio()))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_double():
    return(list(map(float,fastio().split())))
def in_list_str():
    return(fastio().split())

def calcula_sensor(x,h,m):
    QT = (h * 60) // m
    media = sum(x[:QT])/QT
    delta = sum(map(lambda y: (y - media)**2,x[:QT]))
    f = ((delta)/ (QT - 1))**(1/2) 
    return f

resultados = []
while True:
    x = in_list_int()
    if not x:
        break
    H,M = x
    leituras = in_list_double()
    resultados.append(f"{calcula_sensor(leituras,H,M):.5f}")

sys.stdout.write("\n".join(map(str, resultados)))