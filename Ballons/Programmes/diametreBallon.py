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

