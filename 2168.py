N = int(input())

M = []
for i in range(N+1):
    M.append([int(x) for x in input().split()])

Q = N ** 2

STATUS = ""
S = 0
CAM = 0
X = 0
Y = 0
for i in range(1,Q+1):
    if M[X][Y] == 1:
        CAM += 1
    if M[X][Y+1] == 1:
        CAM += 1
    if M[X+1][Y] == 1:
        CAM += 1
    if M[X+1][Y+1] == 1:
        CAM += 1
    if CAM >= 2:
        STATUS += 'S'
    else:
        STATUS += 'U'
    CAM = 0
    Y += 1
    if i % N == 0:
        Y = 0
        X += 1
        if not i == Q:
            STATUS += '\n'
print(STATUS)