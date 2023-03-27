from heapq import heappush, heappop
from math import inf

class Error(Exception):
    pass

class AlgorithmNotExecutedError(Error):
    def __init__(self,message="O Algoritmo deve ser executado antes de apresentar o caminho!",*args, **kwargs):
        self.message = message
        super().__init__(self.message,*args, **kwargs)

class Grafo():
    def __init__(self,arestas):
        super().__init__()
        self.adj = {}
        self.arestas = arestas
        self.executado = False

    def addAresta(self,v1,v2,custo):
        if v1 in self.adj.keys():
            self.adj[v1].append((v2,custo))
        else:
            self.adj[v1] = [(v2,custo)]

    def dijkstra(self,origem,destino):
        self.origem = origem
        self.destino = destino
        self.prev = [None] * self.arestas

        dist = [inf] * self.arestas
        visitados = [False] * self.arestas

        pq = []

        dist[origem] = 0
        heappush(pq,(dist[origem],origem))

        while not len(pq) == 0:
            p = heappop(pq)
            u = p[1]

            if not visitados[u]:
                visitados[u] = True
                if u in self.adj.keys():
                    for no in self.adj[u]:
                        v = no[0]
                        custo = no[1]

                        if dist[v] > dist[u] + custo:
                            dist[v] = dist[u] + custo
                            heappush(pq,(dist[v],v))
                            self.prev[v] = u
        self.executado = True
        return dist[destino]

    def getPath(self):
        if not self.executado:
            raise AlgorithmNotExecutedError()
        s = []
        u = self.destino
        if self.prev[self.destino] != None or u == self.origem:
            while u != None:
                s.insert(0,u)
                u = self.prev[u]
        return s

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
            p_entrada = [int(x) for x in input().split()]
            p_linha1 = [int(x) for x in input().split()]
            p_linha2 = [int(x) for x in input().split()]
            linhas = [p_linha1,p_linha2]
            p_transicao_1_2 = [int(x) for x in input().split()]
            p_transicao_2_1 = [int(x) for x in input().split()]
            transicoes = [p_transicao_1_2,p_transicao_2_1]
            p_saida = [int(x) for x in input().split()]
            tam_entrada = len(p_entrada)
            tam_linha_1 = len(p_linha1) 
            tam_transicao_1_2 = len(p_transicao_1_2)
            tam_linha_2 = len(p_linha2) 
            tam_transicao_2_1 = len(p_transicao_2_1)
            tam_saida = len(p_saida)
            arestas =  tam_entrada + tam_linha_1 + tam_linha_2 + tam_transicao_1_2 + tam_transicao_2_1 + tam_saida 
            
            grafo = Grafo(arestas+2)
            n_aresta = 0
            nos_entradas = []
            nos_producao_1 = []
            nos_transicao_1 = []
            nos_producao_2 = []
            nos_transicao_2 = []
            nos_saidas = []
            for i in range(tam_entrada):
                nos_entradas.append(n_aresta)
                n_aresta += 1

            for i in range(tam_saida):
                nos_saidas.append(n_aresta)
                n_aresta += 1

            for i in range(tam_linha_1):
                nos_producao_1.append(n_aresta)
                n_aresta += 1
                nos_producao_2.append(n_aresta)
                n_aresta += 1

            for i in range(tam_transicao_1_2):
                nos_transicao_1.append(n_aresta)
                n_aresta += 1
                nos_transicao_2.append(n_aresta)
                n_aresta += 1

            destino1, destino2 = arestas, arestas+1

            grafo.addAresta(nos_entradas[0],nos_producao_1[0],p_entrada[0])
            grafo.addAresta(nos_entradas[1],nos_producao_2[0],p_entrada[1])

            grafo.addAresta(nos_producao_1[-1],nos_saidas[0],p_linha1[-1])
            grafo.addAresta(nos_producao_2[-1],nos_saidas[1],p_linha2[-1])

            grafo.addAresta(nos_saidas[0],destino1,p_saida[0])
            grafo.addAresta(nos_saidas[1],destino2,p_saida[1])

            for i in range(tam_linha_1-1):
                grafo.addAresta(nos_producao_1[i],nos_producao_1[i+1],p_linha1[i])
                grafo.addAresta(nos_producao_1[i],nos_transicao_1[i],p_linha1[i])
                grafo.addAresta(nos_producao_2[i],nos_producao_2[i+1],p_linha2[i])
                grafo.addAresta(nos_producao_2[i],nos_transicao_2[i],p_linha2[i])

            for i in range(0,tam_transicao_1_2):
                grafo.addAresta(nos_transicao_1[i],nos_producao_2[i+1],p_transicao_1_2[i])
                grafo.addAresta(nos_transicao_2[i],nos_producao_1[i+1],p_transicao_2_1[i])

            distancias = [0] * 4
            distancias[0] = grafo.dijkstra(nos_entradas[0],destino1)
            distancias[1] = grafo.dijkstra(nos_entradas[0],destino2)
            distancias[2] = grafo.dijkstra(nos_entradas[1],destino1)
            distancias[3] = grafo.dijkstra(nos_entradas[1],destino2)

            resultados.append(min(distancias))

    except EOFError:
        break


for resultado in resultados:
    print(resultado)