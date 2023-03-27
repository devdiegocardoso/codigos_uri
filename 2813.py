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

dias = in_int()
previsoes = [in_list_str() for _ in range(dias)]
print(previsoes)
sol = "sol"
chuva = "chuva"
guarda_chuvas = [0] * 2
for x in range(dias):
    atual = previsoes[x]
    if atual[0] == sol and atual[1] == chuva:
        guarda_chuvas[1] += 1
    elif atual[0] == chuva and atual[1] == sol:
        guarda_chuvas[0] += 1
    elif atual[0] == chuva and atual[1] == chuva:
        guarda_chuvas[0] += 1
print(guarda_chuvas)

        