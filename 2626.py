from enum import Enum

class Jogada(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

def converter(jogadas):
    lista = []
    for item in jogadas:
        if item == 'papel':
            lista.append(Jogada.PAPEL)
        elif item == 'pedra':
            lista.append(Jogada.PEDRA)
        else:
            lista.append(Jogada.TESOURA)
    return lista

def venceu(j1,j2):
    if (j1 == Jogada.PAPEL and j2 == Jogada.PEDRA) or (j1 == Jogada.PEDRA and j2 == Jogada.TESOURA) or (j1 == Jogada.TESOURA and j2 == Jogada.PAPEL):
        return True
    return False

def verifica_turno(jogadas):
    if venceu(jogadas[0],jogadas[1]) and venceu(jogadas[0],jogadas[2]):
        print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
    elif venceu(jogadas[1],jogadas[0]) and venceu(jogadas[1],jogadas[2]):
        print('Iron Maiden\'s gonna get you, no matter how far!')
    elif venceu(jogadas[2],jogadas[0]) and venceu(jogadas[2],jogadas[1]):
        print('Urano perdeu algo muito precioso...')
    else:
        print('Putz vei, o Leo ta demorando muito pra jogar...')

while True:
    try:
        jogadas = [str(x) for x in input().split()]
        jogadas_c = converter(jogadas)
        verifica_turno(jogadas_c)
    except EOFError:
        break