N = int(input())
somatorio = 0

for i in range(N):
    vet = input()
    valores = vet.split(" ")
    media = ((float(valores[0]) * 2) + (float(valores[1]) * 3) + (float(valores[2]) * 5)) / 10
    print("{:.1f}".format(media))
    
