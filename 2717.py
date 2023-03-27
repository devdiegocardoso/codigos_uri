M = int(input())
A, B = [int(x) for x in input().split()]

if A + B <= M:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")
