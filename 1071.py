X = int(input())
Y = int(input())
tmp = 0
if X > Y:
    tmp = X
    X = Y
    Y = tmp
somatorio = 0
for i in range(X+1,Y):
    if i % 2 != 0:
        somatorio += i

print(somatorio)
