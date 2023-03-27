fd, bd, md = [int (x) for x in input().split()]
fr, br, mr = [int (x) for x in input().split()]

na = 0
if fd < fr:
    na += fr - fd

if bd < br:
    na += br - bd

if md < mr:
    na += mr - md

print(na)
