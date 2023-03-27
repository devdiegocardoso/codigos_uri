def is_prime(N):
    if N < 2:
        return False
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

str_result = []
success = "You’re a coastal aircraft, Robbie, a large silver aircraft."
failure = "Bad boy! I’ll hit you."

while True:
    try:
        v = []
        m = int(input())
        for i in range(0,m):
            v.append(int(input()))
        n = int(input())
        soma = sum([v[x] for x in range(m-1,-1,-n)])
        str_result.append(success if is_prime(soma) else failure)
    except EOFError:
        break

for linha in str_result:
    print(linha)