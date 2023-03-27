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

L = in_int()
C = in_int()

T1 = (L * C) + ((L-1)*(C-1))
T2 = ((L-1) * 2) + ((C-1) * 2)

print(T1)
print(T2)
