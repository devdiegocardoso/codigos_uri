largura = 39
altura = 7

l = 1

while l <= altura:
    c = 1
    while c <= largura:
        if l == 1 or l == altura:
            print("-",end='')
        elif c == 1 or c == largura:
            print('|',end='')
        else:
            print(' ',end='')
        if l == 2 and c == 9:
            print("Roberto",end='')
            c += len("Roberto")
        elif l == 4 and c == 9:
            print("5786",end='')
            c += len("5786")
        elif l == 6 and c == 9:
            print("UNIFEI",end='')
            c += len("UNIFEI")
        c += 1
    l += 1
    print()
        