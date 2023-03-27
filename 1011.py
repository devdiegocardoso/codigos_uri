# -*- coding: utf-8 -*-

PI = 3.14159
def volume(R):
    A = (4.0/3.0)*PI*(R**3)
    return A

R = float(input())
print('VOLUME = {:0.3f}'.format(volume(R)))
