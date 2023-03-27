N = int(input())

low = 10
high = 20

in_q = 0
out_q = 0

for i in range(N):
    V = int(input())
    if V >= low and V <= high:
        in_q += 1
    else:
        out_q += 1

print("{} in".format(in_q))
print("{} out".format(out_q))

        
