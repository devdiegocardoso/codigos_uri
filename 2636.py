import functools
import sys

fastio = sys.stdin.readline
def in_int():
    return(int(fastio()))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_str():
    return(fastio().split())

# @functools.lru_cache(maxsize=128)
# def sieve(n):        
#     primes = 2*[False] + (n-1)*[True]
#     for i in range(2, int(n**0.5+1.5)):
#         for j in range(i*i, n+1, i):
#             primes[j] = False
#     return [prime for prime, checked in enumerate(primes) if checked]

def sieve(N):
    marcacao = [True]*N
    primos = []
    append = primos.append
    for x in range(2,N):
        if marcacao[x] == True:
            append(x)
            for m in range(x+x,N,x):
                marcacao[m] = False
    return primos

resultados = []
if __name__ == "__main__":

    list_p = sieve(1000000)
    list_p.pop(0)
    
    while True:
        N = in_int()
        if N == 0:
            break
        c = 0
        fator = list_p[c]
        fatores = []
        entrada = N
        while 1:
            if N % fator == 0:
                N /= fator
                fatores.append(fator)
            if len(fatores) == 2:
                fatores.append(int(entrada / (fatores[0]*fatores[1])))
                break
            c += 1
            fator = list_p[c]
        resultados.append(f"{entrada} = {fatores[0]} x {fatores[1]} x {fatores[2]}\n")
    sys.stdout.write("".join(resultados))
