lista_jogadores = []
lista_reprovados = []
lista_operacoes = []

def imprime_lista(lista):
    lista.sort()
    for i in range(len(lista)-1):
        print(lista[i],end=' ')
    print(lista[len(lista)-1])


def acertou(x,y,z,o):
    if o == '+':
        return True if soma(x,y) == z else False
    if o == '-':
        return True if sub(x,y) == z else False
    if o == '*':
        return True if mul(x,y) == z else False
    if o == 'I':
        return impossivel(x,y,z)

def soma(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def impossivel(x,y,z):
    return not((x+y==z)or(x-y==z)or(x*y==z))

while True:
    try:
        N = int(input())
        lista_jogadores.clear()
        lista_operacoes.clear()
        lista_reprovados.clear()
        passados = 0
        for i in range(N):
            ENTRY = input().split()
            S_ENTRY = ENTRY[1].split('=')
            OP1 = int(ENTRY[0])
            OP2 = int(S_ENTRY[0])
            R = int(S_ENTRY[1])
            sublista = []
            sublista.append(OP1)
            sublista.append(OP2)
            sublista.append(R)
            lista_operacoes.append(sublista)
        for i in range(N):
            Nome, Escolha, Operador = input().split()
            sublista = []
            sublista.append(Nome)
            sublista.append(int(Escolha))
            sublista.append(Operador)
            lista_jogadores.append(sublista)
        for i in range(N):
            jogador = lista_jogadores[i]
            operacao = lista_operacoes[jogador[1]-1]

            if acertou(operacao[0],operacao[1],operacao[2],jogador[2]):
                passados += 1
            else:
                lista_reprovados.append(jogador[0])
        if passados == 0:
            print("None Shall Pass!")
        elif passados == N:
            print("You Shall All Pass!")
        else:
            imprime_lista(lista_reprovados)
    except EOFError:
        break

