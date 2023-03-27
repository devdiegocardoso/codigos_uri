notas = [100,50,20,10,5,2]
moedas = [100,50,25,10,5,1]
moedas_conv = [1.00,0.50,0.25,0.10,0.05,0.01]
qtde1 = [0] * len(notas)
qtde2 = [0] * len(moedas)

def tNotas(V):
    for i,nota in enumerate(notas):
        qtde1[i] = V // nota
        V = V % nota
    return V

def tMoedas(V):
    for i,moeda in enumerate(moedas):
        qtde2[i] = V // moeda
        V = V % moeda

valor = input().split('.')
VNOTAS = int(valor[0])
VMOEDAS = int(valor[1])
S = tNotas(VNOTAS)
if(S > 0):
    tMoedas(VMOEDAS+100)
else:
    tMoedas(VMOEDAS)

print("NOTAS:")
for i, data in enumerate(qtde1):
    print("{0} nota(s) de R$ {1}.00".format(data,notas[i]))
print("MOEDAS:")
for i, data in enumerate(qtde2):
    print("{0} moeda(s) de R$ {1:0.2f}".format(data,moedas_conv[i]))
