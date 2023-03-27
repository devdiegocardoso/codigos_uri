import math
def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

P1 = input().split()
P2 = input().split()

print("{:0.4f}".format(dist(float(P1[0]),float(P1[1]),float(P2[0]),float(P2[1]))))
