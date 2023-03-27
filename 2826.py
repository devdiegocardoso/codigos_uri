import sys

fastio = sys.stdin.readline
def in_str():
    return fastio().replace("\n",'')
def in_int():
    x = fastio()
    if not x:
        return None
    return(int(x))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_double():
    return(list(map(float,fastio().split())))
def in_list_str():
    return(fastio().split())

p1 = in_str()
p2 = in_str()

maior, menor = (p1,p2) if len(p1) > len(p2) else (p2,p1)
lexico = []
found = False
for i,c in enumerate(menor):
    if ord(p1[i]) < ord(p2[i]):
        lexico.extend([p1,p2])
        found = True
    elif ord(p1[i]) > ord(p2[i]):
        lexico.extend([p2,p1])
        found = True
    if found:
        break

if not found:
    lexico.extend([menor,maior])

sys.stdout.write("\n".join(lexico))
print()