largura = 39
altura = 20

l = 1

inteiros = [x for x in range(0,16)]
octal = [oct(x)[2:] for x in inteiros]
hexa = [hex(x)[2:].upper() for x in inteiros]
inteiros = [str(x) for x in inteiros]

while l <= altura:
    c = 1
    while c <= largura:
        if l == 1 or l == altura or l == 3:
            print("-",end='')
        elif c == 1 or c== 13 or c == 23 or c == largura:
            print('|',end='')
        else:
            print(' ',end='')
        
        if l == 2 and c == 3:
            print('decimal',end='')
            c+= len('decimal')
        if l == 2 and c == 15:
            print('octal',end='')
            c+= len('octal')
        if l == 2 and c == 25:
            print('Hexadecimal',end='')
            c+= len('hexadecimal')

        if l > 3 and l < altura:
            if c == 6 and len(inteiros[l-4]) > 1:
                print(inteiros[l-4],end='')
                c+= len(inteiros[l-4])
            elif c == 7 and len(inteiros[l-4]) == 1:
                print(inteiros[l-4],end='')
                c+= len(inteiros[l-4])
            if c == 16 and len(octal[l-4]) > 1:
                print(octal[l-4],end='')
                c+= len(octal[l-4])
            elif c == 17 and len(octal[l-4]) == 1:
                print(octal[l-4],end='')
                c+= len(octal[l-4])
            if c == 29 and len(hexa[l-4]) > 1:
                print(hexa[l-4],end='')
                c+= len(hexa[l-4])
            elif c == 30 and len(hexa[l-4]) == 1:
                print(hexa[l-4],end='')
                c+= len(hexa[l-4])
        c += 1
    l += 1
    print()
        