T = int(input())

class Circulo():
    def __init__(self,x,y,r):
        self.radius = r
        self.x = x
        self.y = y

class Retangulo():
    def __init__(self,w,h,x,y):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.MW = w/2
        self.MH = h/2

def intersect(c,r):
    cx = abs(c.x - r.x - r.MW)
    xDist = r.MW + c.radius
    if cx > xDist:
        return False
    cy = abs(c.y - r.y - r.MH)
    yDist = r.MH + c.radius
    if cy > yDist:
        return False
    if cx <= r.MW or cy <= r.MH:
        return True
    
    xCornerDist = cx - r.MW
    yCornerDist = cy - r.MH

    xCornerDist2 = xCornerDist * xCornerDist
    yCornerDist2 = yCornerDist * yCornerDist

    maxCornerDist = c.radius * c.radius

    return xCornerDist2 + yCornerDist2 <= maxCornerDist

tabela = {
    'fire':[200,20,30,50],
    'water':[300,10,25,40],
    'earth':[400,25,55,70],
    'air':[100,18,38,60]
}


lista = []

for i in range(T):
    w,h,x0,y0 = [int(x) for x in input().split()]
    tipo,nivel,cx,cy = [x for x in input().split()]
    nivel = int(nivel)
    cx = int(cx)
    cy = int(cy)
    encontrado = False
    r = Retangulo(w,h,x0,y0)
    c = Circulo(cx,cy,tabela[tipo][nivel])
    # if intersect(c,r):
    #     print(tabela[tipo][0])
    # else:
    #     print(0)

    if intersect(c,r):
        lista.append(tabela[tipo][0])
    else:
        lista.append(0)

for item in lista:
    print(item)
    
    