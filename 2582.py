musicas = ['PROXYCITY' , 'P.Y.N.G.' , 'DNSUEY!' , 'SERVERS' , 'HOST!' , 'CRIPTONIZE' , 'OFFLINE DAY' , 'SALT' , 'ANSWER!' , 'RAR?' , 'WIFI ANTENNAS']

N = int(input())

for i in range(0,N):
    b1, b2 = [int(x) for x in input().split()]
    print(musicas[b1+b2])