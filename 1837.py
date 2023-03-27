v = input().split(" ")
A = int(v[0])
B = int(v[1])

q = A // B
r = A % B

if r < 0:
    r += abs(B)
    q += 1
print("{0} {1}".format(q,r))
