while True:
    try:
        QP = int(input())
        pesquisadas = []
        for i in range(QP):
            pesquisadas.append(input())
        TP = int(input())
        for i in range(TP):
            total = 0
            maior = -1
            pesquisa = input()
            for palavra in pesquisadas:
                if palavra.find(pesquisa) == 0:
                    total += 1
                    if len(palavra) > maior:
                        maior = len(palavra)
            if total > 0:
                print("{0} {1}".format(total,maior))
            else:
                print(-1)
    except EOFError:
        break