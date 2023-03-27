grupos = {
    1: 'a',
    2: 'd',
    3: 'g',
    4: 'j',
    5: 'm',
    6: 'p',
    7: 's',
    8: 'v',
    9: 'y',
}

def converteParaLetra(pontos):
    grupo = len(pontos)
    char = ord(grupos[grupo])+len(pontos[0])-1
    return chr(char)

decodificado = []
while True:
    try:
        letras = int(input())

        for i in range(letras):
            pontos = input().split()
            decodificado.append(converteParaLetra(pontos))
    except EOFError:
        break 
    
for letra in decodificado:
    print(letra)