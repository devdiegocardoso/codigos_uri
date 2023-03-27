import re

codes = {
    -1:"FAILURE",
    1: "MONDAY",
    2: "MONDAY",
    3: "TUESDAY",
    4: "TUESDAY",
    5: "WEDNESDAY",
    6: "WEDNESDAY",
    7: "THURSDAY",
    8: "THURSDAY",
    9: "FRIDAY",
    0: "FRIDAY"
}

ex = re.compile('^[A-Z]{3}-[0-9]{4}$')

def verificaDigitos(placa):
    return int(placa[-1])


def validaPlaca(placa):
    if(ex.match(placa)):
        return verificaDigitos(placa)
    return -1
    
        

N = int(input())

for i in range(N):
    placa = input()
    print(codes[validaPlaca(placa)])