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

# def sieve(N):
#     primes = []
#     append = primes.append 
#     marcacao = [x for x in range(2,N)]
#     prime = 1
#     while prime * prime < N:
#         number = marcacao[0]
#         marcacao = list(set(marcacao) - set(map(lambda x: x*number,marcacao)))
#         prime = marcacao.pop(0)
#         append(prime)

#     return primes.extend(marcacao)

# def sieve(N):
#     vetor = [x for x in range(3,N+1,2)]
#     meio = N//2
#     inicio = 4

#     for i in range(3,N+1,2):
#         for j in range(inicio,meio,i):
#             vetor[j-1] = 0
#         inicio += 2*(i+1)
#         if inicio > meio:
#             return [2] + list(filter(None,vetor))

# factors := [ ]
# while div(n, 2) = true do
#     factors := add(2, factors)
#     n := n / 2
# while div(n, 3) = true do
#     factors := add(3, factors)
#     n := n / 3
# while div(n, 5) = true do
#     factors := add(5, factors)
#     n := n / 5
# k := 7; i := 1
# while k * k ≤ n do
#     if div(n, k) = true then 
#         add(k, factors)
#         n := n / k
#     else
#         k := k + inc[i]
#         if i < 8 then i := i + 1 else i := 1
# return add(n, factors)

def factorize(N):
    fatores = []
    inc = [4, 2, 4, 2, 4, 6, 2, 6]
    while N % 2 == 0:
        fatores.append(2)
        N = N / 2
    while N % 3 == 0:
        fatores.append(3)
        N = N / 3
    while N % 5 == 0:
        fatores.append(5)
        N = N / 5
    k = 7
    i = 0
    while k * k <= N:
        if N % k == 0:
            fatores.append(k)
            N = N / k
        else:
            k = k + inc[i]
            if i < 7:
                i += 1
            else:
                i = 0
    fatores.append(int(N))
    return fatores 
    

resultados = []
if __name__ == "__main__":

    #list_p = sieve(1000000)

    while True:
        N = in_int()
        if N == 0:
            break
        c = 0
        #fator = list_p[c]
        fatores = []
        entrada = N
        # while 1:
        #     if N % fator == 0:
        #         N /= fator
        #         fatores.append(fator)
        #     if len(fatores) == 2:
        #         fatores.append(int(entrada / (fatores[0]*fatores[1])))
        #         break
        #     c += 1
        #     fator = list_p[c]
        fatores = factorize(N)
        resultados.append(f"{entrada} = {fatores[0]} x {fatores[1]} x {fatores[2]}\n")
    sys.stdout.write("".join(resultados))
