renas = {
    1:'Dasher',
    2:'Dancer',
    3:'Prancer',
    4:'Vixen',
    5:'Comet',
    6:'Cupid',
    7:'Donner',
    8:'Blitzen',
    0:'Rudolph'
}

bolas = [int(x) for x in input().split()]
print(renas[(sum(bolas) % 9)])

