vet = input().split(" ")

for i in range(len(vet)):
    vet[i] = int(vet[i])

A = vet[0]
N = vet[1]
C = 2
while N <= 0:
    N = vet[C]
    C += 1

soma = 0
for i in range(N):
    soma += A + i

print(soma)
