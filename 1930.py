V = input().split(" ")
tomadas = 0
for item in V:
    tomadas += int(item)

print(tomadas-(len(V)-1))

