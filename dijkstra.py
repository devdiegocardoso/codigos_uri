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
