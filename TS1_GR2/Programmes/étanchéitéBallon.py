from math import *

largeur = 0.43
cone = 0.53
surface = 2 * (cone * largeur + largeur)

print("surface =", surface, "m^-3")

volume = 0.25
force = 10.90 * volume
pression = force / surface

print("force =", force, "N")
print("pression =", pression, "Pa")

epaisseur = 100e-6
permeabilite = 1.54e-2

fuitemol = permeabilite * epaisseur * (pression / epaisseur)
print("fuite =", fuitemol, "mol.s^-1")

volmolhel = 22.414e-3
fuitevol = fuitemol * volmolhel
print("fuite =", fuitevol, "m3")
