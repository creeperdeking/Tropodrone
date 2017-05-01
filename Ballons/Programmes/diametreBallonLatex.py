from math import *

def volCone(diametre):
	didiag = sqrt(diametre ** 2 * 2) / 2
	h = didiag * tan(pi / 3)
	base = diametre ** 2
	return base * h / 3

def volTube(diametre):
	return diametre ** 2


def volume(diametre):
	return 2 * volCone(diametre) + volTube(diametre)

etape = 1
largeur = 1
vol = volume(largeur)
cible = 0.25 # Le volume souhaite
# La difference tolere entre le volume souhaite
# et le volume de la largeur calcule.
epsilon = 1e-6
while abs(vol - cible) > epsilon:
	if vol < cible:
		largeur += etape
	else:
		largeur -= etape
	etape /= 2
	vol = volume(largeur)

print("volume =", vol)
print("largeur ballon =", largeur)


