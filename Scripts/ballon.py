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
	rayon = diametre / 2
	h = diametre * sin(pi / 3)
	base = diametre ** 2
	return base * h / 3

def volTube(diametre):
	return diametre ** 2


def volume(diametre):
	return 2 * volCone(diametre) + volTube(diametre)


shift = 1
diametre = 1
vol = volume(diametre)
cible = 0.1
epsilon = 1e-4
while abs(vol - cible) > epsilon:
	if vol < cible:
		diametre += shift
	else:
		diametre -= shift
	shift /= 2
	vol = volume(diametre)

	#print("volume cone = ", volCone(diametre))
	#print("volume tube = ", volTube(diametre))
	print("volume = %f, diametre = %f" % (vol, diametre))

"""

Rapport:

0.47 donne un volume de 0.2508 m2. Les cones sont alors d'une hauteur de 0.2035 m.
Une maquette au 1/5 est reproduite.

"""

