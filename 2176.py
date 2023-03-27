M = input()

bits = 0
R = M
for S in M:
    if S == '1':
        bits += 1

if bits % 2 == 0:
    R += '0'
else:
    R += '1'

print(R)