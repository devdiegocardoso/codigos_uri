jogo = [0] * 5
for i in range(5):
    jogo[i] = [0] * 5

#PEDRA 0
#PAPEL 1
#TESOURA 2
#LAGARTO 3
#SPOCK 4

dict = {"pedra":0,"papel":1,"tesoura":2,"lagarto":3,"Spock":4}

jogo[0][1] = 2
jogo[0][2] = 1
jogo[0][3] = 1
jogo[0][4] = 2

jogo[1][0] = 1
jogo[1][2] = 2
jogo[1][3] = 2
jogo[1][4] = 1

jogo[2][0] = 2
jogo[2][1] = 1
jogo[2][3] = 1
jogo[2][4] = 2

jogo[3][0] = 2
jogo[3][1] = 1
jogo[3][2] = 2
jogo[3][4] = 1

jogo[4][0] = 1
jogo[4][1] = 2
jogo[4][2] = 1
jogo[4][3] = 2
def vencedor(P1,P2):
    return jogo[dict[P1]][dict[P2]] 
    
N = int(input())

for i in range(N):
    escolhas = input().split(" ")
    P1 = escolhas[0]
    P2 = escolhas[1]
    if vencedor(P1,P2) == 2:
        print("Caso #{}: Raj trapaceou!".format(i+1))
    elif vencedor(P1,P2) == 1:
        print("Caso #{}: Bazinga!".format(i+1))
    else:
        print("Caso #{}: De novo!".format(i+1))
        
