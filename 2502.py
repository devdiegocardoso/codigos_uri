while True:
    try:
        C, N = [int(x) for x in input().split()]
        SUB1 = input()
        SUB2 = input()
        for i in range(N):
            cifrado = input()
            decifrado = ""
            indice = -1
            nova_letra = ""
            for caracter in cifrado:
                nova_letra = caracter
                capitalizado = True if caracter.isupper() else False
                if caracter.lower() in SUB1:
                    indice = SUB1.find(caracter.lower())
                    nova_letra = SUB2[indice].upper() if capitalizado else SUB2[indice].lower()
                elif caracter.upper() in SUB1:
                    indice = SUB1.find(caracter.upper())
                    nova_letra = SUB2[indice].upper() if capitalizado else SUB2[indice].lower()
                elif caracter.lower() in SUB2:
                    indice = SUB2.find(caracter.upper())
                    nova_letra = SUB1[indice].upper() if capitalizado else SUB1[indice].lower()
                elif caracter.upper() in SUB2:
                    indice = SUB2.find(caracter.upper())
                    nova_letra = SUB1[indice].upper() if capitalizado else SUB1[indice].lower()
                decifrado += nova_letra
            print(decifrado)
        print()
    except EOFError:
        break
