line = ''
qtde_jipes = 0
qtde_pessoas = 0

while line != 'ABEND':
    line = input()
    if line != 'ABEND':
        tipo , qtde = line.split()
        if tipo == 'SALIDA':
            qtde_jipes += 1
            qtde_pessoas += int(qtde)
        else:
            qtde_jipes -= 1
            qtde_pessoas -= int(qtde)

print(qtde_pessoas)
print(qtde_jipes)
