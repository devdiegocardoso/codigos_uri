# -*- coding: utf-8 -*-

def triangulo(A,C):
    return (A*C)/2.0
def circulo(C):
    return 3.14159 * (C**2)
def trapezio(A,B,C):
    return ((A+B)*C)/2.0
def quadrado(B):
    return B*B
def retangulo(A,B):
    return A*B

S = input().split()

A = float(S[0])
B = float(S[1])
C = float(S[2])

print('TRIANGULO: {:0.3f}'.format(triangulo(A,C)))
print('CIRCULO: {:0.3f}'.format(circulo(C)))
print('TRAPEZIO: {:0.3f}'.format(trapezio(A,B,C)))
print('QUADRADO: {:0.3f}'.format(quadrado(B)))
print('RETANGULO: {:0.3f}'.format(retangulo(A,B)))
