values = input()
string_v = values.split(" ")

A = int(string_v[0])
B = int(string_v[1])

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
