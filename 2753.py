v = 97
n = [x for x in range(v,v+26)]
o = [chr(x) for x in n]

for i in range(0,len(n)):
    print(f"{n[i]} e {o[i]}")