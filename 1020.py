def idade(DIAS):
    A = DIAS // 365
    R = DIAS % 365
    M = R // 30
    R = R % 30
    D = R
    print("{0} ano(s)\n{1} mes(es)\n{2} dia(s)".format(A,M,D))

idade(int(input()))
    
