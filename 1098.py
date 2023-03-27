import math
i = 0
while i < 2:
    for j in range(1,4):
        diff = math.ceil(i) - i
        if diff > 0.1:
            print("I={0:.1f} J={1:.1f}".format(i,j+i))
        else:
            print("I={0} J={1}".format(math.ceil(i),int(j+i)))
    i += 0.2
