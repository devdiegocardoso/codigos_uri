SEQUENCIA = []

while True:
    try:
        S = input()
        SEQUENCIA.append(S)
    except EOFError:
        break

set_joias = set(SEQUENCIA)
print(len(set_joias))
