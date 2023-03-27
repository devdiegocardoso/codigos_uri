A1 = int(input())
A2 = int(input())
A3 = int(input())

T1 = A2 * 2 + A3 * 4
T2 = A1 * 2 + A3 * 2
T3 = A2 * 2 + A1 * 4

menor = T1

if T2 <= T1 and T2 <= T3:
    menor = T2
elif T3 <= T1 and T3 <= T2:
    menor = T3

print(menor)
