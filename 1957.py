N = int(input())

CODE = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

STR = ""
if N > 0:
    while N > 0:
        INDEX = N % 16
        N = N // 16
        STR += CODE[INDEX]
else:
    STR = CODE[0]


print(STR[::-1])