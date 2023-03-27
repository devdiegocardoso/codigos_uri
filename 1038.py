preco = [4.00,4.50,5.00,2.00,1.50]

def total(codigo,qtde):
    return qtde * preco[codigo-1]

I = input().split()
codigo = int(I[0])
qtde = int(I[1])

print("Total: R$ {:0.2f}".format(total(codigo,qtde)))
