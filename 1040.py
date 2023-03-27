def media(N1,N2,N3,N4):
    media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4))/10
    return media

def tipo(M):
    print("Media: {0:0.1f}".format(M))
    if M >= 7.0:
        print("Aluno aprovado.")
    elif M < 5.0:
        print("Aluno reprovado.")
    elif M >= 5.0 and M < 7:
        print("Aluno em exame.")
        exame = float(input())
        print("Nota do exame: {0:0.1f}".format(exame))
        NM = (M + exame)/2
        if NM >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {0:0.1f}".format(NM))

I = input().split()
N1 = float(I[0])
N2 = float(I[1])
N3 = float(I[2])
N4 = float(I[3])

tipo(media(N1,N2,N3,N4))
