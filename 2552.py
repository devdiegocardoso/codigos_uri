from enum import Enum

class Quadrantes(Enum):
    SuperiorEsquerdo = 1
    SuperiorDireito = 2
    Superior = 3
    Esquerdo = 4
    Direito = 5
    InferiorEsquerdo = 6
    InferiorDireito = 7
    Inferior = 8
    Centro = 9

MAX_L = 0
MAX_C = 0

def quadrante(x,y):
    if x == 0 and y == 0:
        return Quadrantes.SuperiorEsquerdo
    elif x == 0 and y == MAX_C:
        return Quadrantes.SuperiorDireito
    elif x == 0:
        return Quadrantes.Superior
    elif x == MAX_L and y == 0:
        return Quadrantes.InferiorEsquerdo
    elif x == MAX_L and y == MAX_C:
        return Quadrantes.InferiorDireito
    elif x == MAX_L:
        return Quadrantes.Inferior
    elif y == 0:
        return Quadrantes.Esquerdo
    elif y == MAX_C:
        return Quadrantes.Direito
    else:
        return Quadrantes.Centro

def verifica_ponto(ponto,x,y,tabuleiro,configuracao):
    if configuracao[x][y] == 1:
        tabuleiro[x][y] = 9
    else:
        total = 0
        if ponto == Quadrantes.SuperiorEsquerdo:
            if MAX_L == 0:
                total = configuracao[x][y+1]
            elif MAX_C == 0:
                total = configuracao[x+1][y]
            else:
                total = configuracao[x][y+1] + configuracao[x+1][y]
        elif ponto == Quadrantes.SuperiorDireito:
            if MAX_L == 0:
                total = configuracao[x][y-1]
            else:
                total = configuracao[x][y-1] + configuracao[x+1][y]
        elif ponto == Quadrantes.Superior:
            if MAX_L == 0:
                total = configuracao[x][y-1] + configuracao[x][y+1]
            else:
                total = configuracao[x][y-1] + configuracao[x][y+1] + configuracao[x+1][y]
        elif ponto == Quadrantes.InferiorEsquerdo:
            if MAX_C == 0:
                total = configuracao[x-1][y]
            else:
                total = configuracao[x-1][y] + configuracao[x][y+1]      
        elif ponto == Quadrantes.InferiorDireito:
            total = configuracao[x][y-1] + configuracao[x-1][y]
        elif ponto == Quadrantes.Inferior:
            total = configuracao[x][y-1] + configuracao[x][y+1] + configuracao[x-1][y]
        elif ponto == Quadrantes.Esquerdo:
            if MAX_C == 0:
                total = configuracao[x-1][y] + configuracao[x+1][y] 
            else:
                total = configuracao[x-1][y] + configuracao[x+1][y] + configuracao[x][y+1]
        elif ponto == Quadrantes.Direito:
            total = configuracao[x-1][y] + configuracao[x+1][y] + configuracao[x][y-1]
        elif ponto == Quadrantes.Centro:
            total = configuracao[x-1][y] + configuracao[x+1][y] + configuracao[x][y-1] + configuracao[x][y+1]
        tabuleiro[x][y] = total

def print_tab(tabuleiro):
    for i in range(0,len(tabuleiro)):
        for j in range(0,len(tabuleiro[i])):
            print(tabuleiro[i][j],end='')
        print()

while True:
    try:
        i,j = [int(x) for x in input().split()]
        MAX_L = i-1
        MAX_C = j-1
        tab = [[0 for x in range(0,j)]for y in range(0,i)]
        conf = []
        for l in range(0,i):
            conf.append([int(x) for x in input().split()])
        for l in range(0,i):
            for c in range(0,j):
                ponto = quadrante(l,c)
                verifica_ponto(ponto,l,c,tab,conf)
        print_tab(tab)
    except EOFError:
        break
    