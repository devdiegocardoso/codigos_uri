V = input().split(" ")
D1 = int(V[0])
D2 = int(V[1])
D3 = int(V[2])

if D2 < D1 and D3 >= D2:
    print(":)")
elif D2 > D1 and D3 <= D2:
    print(":(")
elif D2 > D1 and D3 > D2:
    Dif1 = D2 - D1
    Dif2 = D3 - D2
    if Dif2 < Dif1:
        print(":(")
    else:
        print(":)")
elif D2 < D1 and D3 < D2:
    Dif1 = D1 - D2
    Dif2 = D2 - D3
    if Dif2 < Dif1:
        print(":)")
    else:
        print(":(")
elif D2 == D1 and D3 > D2:
    print(":)")
else:
    print(":(")

