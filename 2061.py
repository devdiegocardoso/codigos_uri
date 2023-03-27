abas, acoes = [int(x) for x in input().split()]

for i in range(acoes):
    acao = input().strip()
    if acao == "fechou":
        abas += 1
    else:
        abas -= 1
print(abas)