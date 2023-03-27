gritos = 0
grito = "caw caw"
numero = 0
while gritos < 3:
    sequencia = input()
    if sequencia == grito:
        print(numero)
        gritos += 1
        numero = 0
    else:
        olho = 1 
        for piscada in range(len(sequencia)-1,-1,-1):
            if sequencia[piscada] == "*":
                numero += olho
            olho *= 2   
                
                
