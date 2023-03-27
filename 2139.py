class Data:
    def __init__(self,MES,DIA):
        self.MES = MES
        self.DIA = DIA

dias = []

while True:
    try:
        MES, DIA = [int(x) for x in input().split()]
        dias.append(Data(MES,DIA))
    except EOFError:
        break

dias_ano = 366
meses = [31,29,31,30,31,30,31,31,30,31,30,31]
natal = dias_ano - (meses[12-1] - 25)
for dia in dias:
    MES = dia.MES
    DIA = dia.DIA
    SOMA_MES = sum([meses[x] for x in range(MES)])
    dias_faltantes = natal - SOMA_MES + (meses[MES-1] - DIA)
    if dias_faltantes == 0:
        print("E natal!")
    elif dias_faltantes == 1:
        print("E vespera de natal!")
    elif dias_faltantes < 0:
        print("Ja passou!")
    else:
        print("Faltam {} dias para o natal!".format(dias_faltantes))

