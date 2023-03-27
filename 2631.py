def root(data,elem):
    while(data[elem] != elem):
        data[elem] = data[data[elem]]
        elem = data[elem]
    return elem

def find(data,A,B):
    return True if root(data,A) == root(data,B) else False

def weighted_union(data,size,A,B):
    root_A = root(data,A)
    root_B = root(data,B)

    if(size[root_A] < size[root_B]):
        data[root_A] = data[root_B]
        size[root_B] += size[root_A]
    else:
        data[root_B] = data[root_A]
        size[root_A] += size[root_B]

while True:
    try:
        N,M,Q = [int(x) for x in input().split()]
        ligacoes = [x for x in range(N)]
        size = [1] * N
        for i in range(0,M):
            A,B = [int(x)-1 for x in input().split()]
            print(A,B)
            weighted_union(ligacoes,size,A,B)
        for i in range(0,Q):
            A,B = [int(x)-1 for x in input().split()]    
            if find(ligacoes,A,B):
                print('S')
            else:
                print('N')
        print()
    except EOFError:
        break