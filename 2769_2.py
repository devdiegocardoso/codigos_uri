resultados = []
while True:
    try:
        etapas = int(input())
        if etapas == 1:
            p_entrada = [int(x) for x in input().split()]
            linha1 = int(input())
            linha2 = int(input())
            p_saida = [int(x) for x in input().split()]
            r1 = p_entrada[0] + linha1 + p_saida[0]
            r2 = p_entrada[1] + linha2 + p_saida[1]

            resultados.append(r1 if r1 < r2 else r2)
        else:
            p_entrada1, p_entrada2 = [int(x) for x in input().split()]
            p_linha1 = [int(x) for x in input().split()]
            p_linha2 = [int(x) for x in input().split()]
            p_transicao_1_2 = [int(x) for x in input().split()]
            p_transicao_2_1 = [int(x) for x in input().split()]
            p_saida1, p_saida2 = [int(x) for x in input().split()]

            ac1 = p_entrada1 + p_linha1[0]
            ac2 = p_entrada2 + p_linha2[0]
            tempo = ac1 if ac1 < ac2 else ac2
            linha = 1 if ac1 < ac2 else 2
            tam = len(p_linha1)
            for i in range(tam-2):
                if linha == 1:
                    tempo_transicao = p_transicao_1_2[i] + p_linha2[i+1]
                    if tempo_transicao < p_linha1[i]:
                        tempo += tempo_transicao
                        linha = 2
                    else:
                        tempo += p_linha1[i]
                        linha = 1
                else:
                    tempo_transicao = p_transicao_2_1[i] + p_linha1[i+1]
                    if tempo_transicao < p_linha2[i]:
                        tempo += tempo_transicao
                        linha = 1
                    else:
                        tempo += p_linha2[i]
                        linha = 2
            resultados.append(tempo)
                    

    except EOFError:
        break


for resultado in resultados:
    print(resultado)