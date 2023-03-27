import functools
import sys

fastio = sys.stdin.readline
def in_int():
    return(int(fastio()))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_str():
    return(fastio().split())

resultados = []
if __name__ == "__main__":

    while True:
        N = in_int()
        if N == 0:
            break
        fatores = []
        entrada = N
        p = 2
        while p*p <= N:
            if N % p == 0:
                N /= p
                fatores.append(p)
            if len(fatores) == 2:
                fatores.append(int(entrada / (fatores[0]*fatores[1])))
                break
            p += 1
        resultados.append(f"{entrada} = {fatores[0]} x {fatores[1]} x {fatores[2]}\n")
    sys.stdout.write("".join(resultados))
