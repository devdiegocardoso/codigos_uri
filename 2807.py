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

def fib(N):
    a = 1
    b = 1
    for _ in range(N):
        yield a
        a, b = b, b + a

N = int(input())
list_fib = [str(x) for x in fib(N)]
list_fib.reverse()
print(" ".join(list_fib))