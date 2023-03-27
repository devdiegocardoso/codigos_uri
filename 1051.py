salario = float(input())
imposto = 0
if salario >= 0.00 and salario <= 2000.00:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000.00:
    excedente = salario - 2000.00
    imposto = excedente * 0.08
    print("R$ {:.2f}".format(imposto))
elif salario >= 3000.01 and salario <= 4500.00:
    excedente1 = 1000.00
    excedente2 = salario - 3000.00
    imposto = (excedente1 * 0.08) + (excedente2 * 0.18)
    print("R$ {:.2f}".format(imposto))
elif salario > 4500.00:
    excedente1 = 1000.00
    excedente2 = 1500.00
    excedente3 = salario - 4500.00
    imposto = (excedente1 * 0.08) + (excedente2 * 0.18) + (excedente3 * 0.28)
    print("R$ {:.2f}".format(imposto))
