S = 0
j = 1
for i in range(1,40,2):
    S += i/j
    j *= 2
    
print("{:.2f}".format(S))
