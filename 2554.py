def todos_podem(avaliacao, qtde):
    return True if sum(avaliacao) == qtde else False

while True:
    try:
        pode = False
        N,D = [int(x) for x in input().split()]
        pessoas = [[0 for i in range(0,N)] for j in range(0,D)]
        datas = [None for i in range(0,D)]
        for d in range(0,D):
            linha = [x for x in input().split()]
            datas[d] = linha[0]
            for n in range(0,N):
                pessoas[d][n] = int(linha[n+1])
        for linha in enumerate(pessoas):
            if todos_podem(linha[1],N):
                print(datas[linha[0]])
                pode = True
                break
        if not pode:
            print('Pizza antes de FdI')
    except EOFError:
        break