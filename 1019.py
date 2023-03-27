def tempo(S):
    H = S//(60*60)
    R = S%(60*60)
    M = R // 60
    R = S % 60
    S = R
    print("{0}:{1}:{2}".format(H,M,S))

tempo(int(input()))
