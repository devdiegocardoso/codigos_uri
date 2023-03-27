resultados = []
while True:
    try:
        etapas = int(input())
        p_entrada1, p_entrada2 = [int(x) for x in input().split()]
        p_linha1 = [int(x) for x in input().split()]
        p_linha2 = [int(x) for x in input().split()]
        p_linha = [p_linha1,p_linha2]
        p_transicao_1_2 = []
        p_transicao_2_1 = []
        p_transicao = []
        if etapas != 1:
            p_transicao_1_2 = [int(x) for x in input().split()]
            p_transicao_2_1 = [int(x) for x in input().split()]
            p_transicao = [p_transicao_1_2, p_transicao_2_1]
        p_saida1, p_saida2 = [int(x) for x in input().split()]
        
        f1 = [0]*etapas
        f2 = [0]*etapas

        f1[0] = p_entrada1 + p_linha[0][0]
        f2[0] = p_entrada2 + p_linha[1][0]

        f = 0
        for j in range(1,etapas):
            if f1[j-1] + p_linha[0][j] <= f2[j-1] + p_transicao[1][j-1] +  p_linha[0][j]:
                f1[j] = f1[j-1] + p_linha[0][j]
            else:
                f1[j] = f2[j-1] + p_transicao[1][j-1] +  p_linha[0][j]
            if f2[j-1] + p_linha[1][j] <= f1[j-1] + p_transicao[0][j-1] +  p_linha[1][j]:
                f2[j] = f2[j-1] + p_linha[1][j]
            else:
                f2[j] = f1[j-1] + p_transicao[0][j-1] +  p_linha[1][j]
        if f1[etapas-1] + p_saida1 <= f2[etapas-1] + p_saida2:
            f = f1[etapas-1] + p_saida1
        else:
            f = f2[etapas-1] + p_saida2
        resultados.append(f)

    except EOFError:
        break


for resultado in resultados:
    print(resultado)