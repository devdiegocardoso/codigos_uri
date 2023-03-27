lista = []
N = 0
while True:
    try:
        N = input()
        lista.append(int(N))
    except EOFError:
        break
    except Exception:
        break
    
for N in lista:
    if N == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
