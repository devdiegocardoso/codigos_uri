X = int(input())
Y = int(input())
soma = 0

if X > Y:
    tmp = X
    X = Y
    Y = tmp

for i in range(X,Y+1):
    if i % 13 != 0:
        soma += i
print(soma)
