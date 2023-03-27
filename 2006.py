CORRETO = int(input())
RESPOSTAS = [int(x) for x in input().split()]

S = sum([1 for x in RESPOSTAS if x == CORRETO])
print(S)