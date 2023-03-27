cells = []
while 1:
    try:
        line = input()
        cells.append(line)
    except EOFError:
        break

dict_letters = {chr(k):v for v,k in enumerate(range(ord('A'),ord('Z')+1),1)}

for cell in cells:
    indice = 0
    p = 1
    for letter in cell[::-1]:
        indice += dict_letters[letter] * p
        p *= 26
    print(indice if indice <= 16384 else 'Essa coluna nao existe Tobias!')