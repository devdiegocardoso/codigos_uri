N = int(input())

for i in range(N):
    V = int(input())
    if V != 0:
        if V % 2 == 0:
            if V > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        else:
            if V > 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")
    else:
        print("NULL")
