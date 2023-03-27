F1 = 0
F2 = 0
N = int(input())
SEQ = 0
for i in range(1,N+1):
    if i == 1:
        F1 = 0
        F2 = 0
    elif i == 2:
        F1 = 0
        F2 = 1
        SEQ = 1
    else:
        SEQ = F1 + F2
        F1 = F2
        F2 = SEQ
    if i == N:
        print(SEQ)
    else:
        print(SEQ,end=" ")
    
        
