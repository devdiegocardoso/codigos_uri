salario = float(input())

salario_novo = 0
reajuste = 0
percentual = 0

if salario >= 0 and salario <= 400.00:
    salario_novo = salario * 1.15
    percentual = 15
elif salario >= 400.01 and salario <= 800.00:
    salario_novo = salario * 1.12
    percentual = 12
elif salario >= 800.01 and salario <= 1200.00:
    salario_novo = salario * 1.10
    percentual = 10
elif salario >= 1200.01 and salario <= 2000.00:
    salario_novo = salario * 1.07
    percentual = 7
elif salario > 2000.00:
    salario_novo = salario * 1.04
    percentual = 4

reajuste = salario_novo - salario

print("Novo salario: {:.2f}".format(salario_novo))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))

