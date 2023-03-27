def km_l(T,V):
    return (V*T)/12

T = int(input())
V = int(input())

print("{:0.3f}".format(km_l(T,V)))
