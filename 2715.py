def minimiza_carga(v,n):
    if n == 1:
        return v[0]
    elif n == 2:
        return abs(v[0] - v[1])

    divisao = n//2 - 1 if n % 2 == 0 else n//2

    soma1 = sum(v[:divisao+1])
    soma2 = sum(v[divisao+1:])

    dif = soma1 - soma2
    movement = 1 if dif < 0 else -1

    if dif == 0:
        return dif

    found = False
    last_it = abs(dif)
    while not found:
        divisao += movement
        value = v[divisao] if movement == 1 else v[divisao+1]
        soma1 = soma1 + value if movement == 1 else soma1 - value
        soma2 = soma2 - value if movement == 1 else soma2 + value
        current_it = abs(soma1 - soma2)
        if last_it <= current_it:
            return last_it
        last_it = current_it

lista = []
while True:
    try:
        n = int(input())
        v = [int(x) for x in input().split()]

        lista.append(minimiza_carga(v,n))

    except EOFError:
        break

for item in lista:
    print(item)