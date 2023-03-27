dados = [int(x) for x in input().split()]

soma = sum(dados)

if soma >= 24:
    print(soma-24)
elif soma < 0:
    print(24+soma)
else:
    print(soma)