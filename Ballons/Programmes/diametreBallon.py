from math import *

"""

V = b ** 2 * h / 3

h = (b * sin(pi / 3))
h = (b * sqrt(3)) / 2

V = b ** 2 * (b * sqrt(3)) / 6
V = b ** 3 * sqrt(3) / 6

b = (V * 6 / sqrt(3)) ** (1 / 3)


V = b ** 2 (* 1)
b = sqrt(V)


V = 2 * (b ** 3 * sqrt(3) / 6) + b ** 2
V = 2b ** 3 * sqrt(3) / 3 + b ** 2
V = 

"""

def volCone(diametre):
	didiag = sqrt(diametre ** 2 * 2) / 2
	h = didiag * tan(pi / 3)
	base = diametre ** 2
	return base * h / 3

def volTube(diametre):
	return diametre ** 2


def volume(diametre):
	return 2 * volCone(diametre) + volTube(diametre)

def info(vol, largeur):
	print("volume =", vol)
	print("largeur ballon =", largeur)
	diag = sqrt(largeur ** 2 * 2)
	hauteur =  diag / 2 * tan(pi / 3)
	print("hauteur cone =", hauteur)
	print("hauteur total =", hauteur * 2 + 1)
	anglebf = degrees(atan(hauteur / (largeur / 2)))
	print("angle base/face = ", anglebf)
	hauttc = sqrt(hauteur ** 2 + (largeur / 2) ** 2)
	print("hauteur triangle cone =", hauttc)

etape = 1
largeur = 1
vol = volume(largeur)
cible = 0.25
epsilon = 1e-6
count = 0
while abs(vol - cible) > epsilon:
	if vol < cible:
		largeur += etape
	else:
		largeur -= etape
	etape /= 2
	vol = volume(largeur)
	print(count)
	count += 1
info(vol, largeur)

"""

Rapport:

0.47 donne un volume de 0.2508 m2. Les cones sont alors d'une hauteur de 0.2035 m.
Une maquette au 1/5 est reproduite.

"""

