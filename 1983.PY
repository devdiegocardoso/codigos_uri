N = int(input())

ALUNOS = {}
for i in range(N):
    V = input().split()
    ALUNOS[int(V[0])] = float(V[1])

BEST_KEY = max(ALUNOS,key=ALUNOS.get)
BEST_VALUE = max(ALUNOS.values())
if BEST_VALUE >= 8.0:
    print(BEST_KEY)
else:
    print("Minimum note not reached")