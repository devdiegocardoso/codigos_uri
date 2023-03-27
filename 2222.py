N = int(input())
MAX_ELEM = 60

for i in range(1,N+1):
    NC = int(input())
    VO = []
    VC = []
    for i in range(NC):
        VC.append(set(input().split()[1:]))
    NO = int(input())
    for i in range(NO):
        VO.append(input().split())
    for operacao in VO:
        COUNT = 0
        Tipo = operacao[0]
        C1 = int(operacao[1])-1
        C2 = int(operacao[2])-1
        if Tipo == '1':
            print(len(VC[C1] & VC[C2]))
        elif Tipo == '2':
            print(len(VC[C1] | VC[C2]))