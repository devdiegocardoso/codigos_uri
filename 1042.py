valores = input()
string_v = valores.split(" ")
vet = [0] * 3

for i in range(3):
    vet[i] = int(string_v[i])

for i in range(len(vet)-1):
    for j in range(i+1,len(vet)):
        if vet[j] < vet[i]:
            aux = vet[j]
            vet[j] = vet[i]
            vet[i] = aux
        
for value in vet:
    print(value)

print()

for value in string_v:
    print(int(value))

