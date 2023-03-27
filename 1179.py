par = [0] * 5
impar = [0] * 5
c_par = 0
c_impar = 0

def print_par(V):
    for i in range(len(V)):
        print("par[{0}] = {1}".format(i,V[i]))
def print_impar(V):
    for i in range(len(V)):
        print("impar[{0}] = {1}".format(i,V[i]))

for i in range(15):
    N = int(input())
    if N % 2 == 0:
        if c_par < len(par):
            par[c_par] = N
            c_par += 1
        else:
            print_par(par)
            par = [0]*5
            c_par = 0
            par[c_par] = N
            c_par += 1
    else:
        if c_impar < len(impar):
            impar[c_impar] = N
            c_impar += 1
        else:
            print_impar(impar)
            impar = [0]*5
            c_impar = 0
            impar[c_impar] = N
            c_impar += 1

for i in range(c_impar):
        print("impar[{0}] = {1}".format(i,impar[i]))
for i in range(c_par):
        print("par[{0}] = {1}".format(i,par[i]))
