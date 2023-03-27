values = input()
string_v = values.split(" ")

A = int(string_v[0])
B = int(string_v[1])
T = 0

if A > B:
    A = 24 - A
    T = A + B
elif A < B:
    T = B - A
else:
    T = 24

print("O JOGO DUROU {0} HORA(S)".format(T))
