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

#F = 1 + (n 2) + (n 4)
N = in_int()
F = 1 + ((N*(N-1))/2) + ((N*(N-1)*(N-2)*(N-3)) / (4*3*2))
print(int(F))