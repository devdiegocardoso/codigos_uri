import sys

fastio = sys.stdin.readline
def in_int():
    x = fastio()
    if not x:
        return None
    return(int(x))
def in_list_int():
    return(list(map(int,fastio().split())))
def in_list_double():
    return(list(map(float,fastio().split())))
def in_list_str():
    return(fastio().split())

# def mesclar(v1,v2):
#     c = []
#     global tempo
#     while v1 and v2:
#         if v1[0][0] > v2[0][0]:
#             c.append(v2[0])
#             tempo += v1[0][1] + v2[0][1]
#             v2.pop(0)
#         else:
#             c.append(v1[0])
#             tempo += v1[0][1] + v2[0][1]
#             v1.pop(0)
#     while v1:
#         c.append(v1[0])
#         v1.pop(0)
#     while v2:
#         c.append(v2[0])
#         v2.pop(0)
#     return c

# def mergesort(vetor):
#     n = len(vetor)
#     s = 0
#     if n == 1:
#         return vetor

#     l1 = vetor[:n//2]
#     l2 = vetor[n//2:]

#     l1 = mergesort(l1)
#     l2 = mergesort(l2)

#     return mesclar(l1,l2)
# tempo = 0

# def shellSort(nums):
#     h = 1
#     n = len(nums)
#     global tempo
#     while h > 0:
#             for i in range(h, n):
#                 c = nums[i]
#                 j = i
#                 while j >= h and c[0] < nums[j - h][0]:
#                     tempo += nums[j][1] + nums[j-h][1]
#                     nums[j] = nums[j - h]
#                     j = j - h
#                     nums[j] = c

#             h = int(h / 2.2)
#     return nums
# resultados = []
# while True:
#     x = in_int()
#     tempo = 0
#     if not x:
#         break
#     pares = [(x,y) for x,y in zip(in_list_int(),in_list_int())]
#     shellSort(pares)    
#     resultados.append(tempo)
# sys.stdout.write("\n".join(map(str, resultados)))
# print()



#a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
# a = [3,1,2,5,4]
# b = [10,23,15,18,30]
# c = list(zip(a,b))
# print(c)
# print(mergesort(c))
# print(tempo)



# resultados = []
# while True:
#     x = in_int()
#     if not x:
#         break
#     pares = [(x,y) for x,y in zip(in_list_int(),in_list_int())]

#     total = 0
#     ordenado = False
#     while not ordenado:
#         ordenado = True
#         for i in range(1,x-1,2):
#             if pares[i][0] > pares[i+1][0]:
#                 total += pares[i][1] + pares[i+1][1]
#                 pares[i],pares[i+1] = pares[i+1],pares[i]
#                 ordenado = False
#         for i in range(0,x-1,2):
#             if pares[i][0] > pares[i+1][0]:
#                 total += pares[i][1] + pares[i+1][1]
#                 pares[i],pares[i+1] = pares[i+1],pares[i]
#                 ordenado = False
#     resultados.append(total)
# sys.stdout.write("\n".join(map(str, resultados)))
# print()

resultados = []
while True:
    try:
        x = int(input())
        pacotes = [int(x) for x in input().split()]
        tempos = [int(x) for x in input().split()]
        total = 0
        for i in range(x):
            for j in range(i,x):
                if pacotes[i] > pacotes[j]:
                    total += (tempos[i] + tempos[j])
        resultados.append(total)
    except EOFError:
        break
sys.stdout.write("\n".join(map(str, resultados)))
print()

# resultados = []
# while True:
#     x = in_int()
#     if not x:
#         break
#     pares = [(x,y) for x,y in zip(in_list_int(),in_list_int())]
#     total = 0
#     ordenado = False
#     while not ordenado:
#         ordenado = True
#         for j in range(0,x-1):
#             if pares[j][0] > pares[j+1][0]:
#                 total += pares[j][1] + pares[j+1][1]
#                 pares[j],pares[j+1] = pares[j+1],pares[j]
#                 ordenado = False
         
#     resultados.append(total)
# sys.stdout.write("\n".join(map(str, resultados)))
# print()

# resultados = []
# while True:
#     x = in_int()
#     if not x:
#         break
#     pares = [(x,y) for x,y in zip(in_list_int(),in_list_int())]

#     total = 0
#     ordenado = False
#     while not ordenado:
#         ordenado = True
#         for i in range(1,x-1,2):
#             if pares[i][0] > pares[i+1][0]:
#                 total += pares[i][1] + pares[i+1][1]
#                 pares[i],pares[i+1] = pares[i+1],pares[i]
#                 ordenado = False
#         for i in range(0,x-1,2):
#             if pares[i][0] > pares[i+1][0]:
#                 total += pares[i][1] + pares[i+1][1]
#                 pares[i],pares[i+1] = pares[i+1],pares[i]
#                 ordenado = False
#     resultados.append(total)
# sys.stdout.write("\n".join(map(str, resultados)))
# print()