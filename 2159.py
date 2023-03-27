from math import log
def aproximados(N):
    MIN = N/log(N)
    MAX = 1.25506 * MIN
    return MIN, MAX

N = int(input())
MIN, MAX = aproximados(N)
print("{0:.1f} {1:.1f}".format(MIN,MAX))