total = int(input())
compradas = int(input())

figurinhas = {int(input()) for _ in range(compradas)}
print(total-len(figurinhas))