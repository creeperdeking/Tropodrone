import math

# Portance ou trainee 
print("")
print("")
print("Calcul de traînée")

P = 0.1785 # kg/m^3 (masse volumique de l'air)
S = float(input("Surface du ballon (m^2) = "))
L = float(input("Diamètre du ballon (m) = "))
V = float(input("Vitesse relative du fluide (en m.s^-1) = "))

## On calcule Cx
nu = 15.6 * pow(10,-6) # Coefficient de viscosité cinématique de l'air à 25°C 
# https://fr.wikipedia.org/wiki/Viscosit%C3%A9_cin%C3%A9matique

# Pour cela, on calcule le nombre de reynolds
Re = (V * L) / nu
print("Re = "+str(Re))

# https://fr.wikipedia.org/wiki/Coefficient_de_tra%C3%AEn%C3%A9e
# Si Re < 1
# Écoulement de Stokes
# Si 1 < Re < 10^3
# Écoulement intermédiaire
# Si Re > 10^3
# Écoulement turbulent
if int(Re) < 1:
    Cx = 24 / Re
elif int(Re) < pow(10,3):
    Cx = 18.5 / pow(Re, 0.6)
elif int(Re) > pow(10,3):
    Cx = 0.44

Fx = 0.5 * P * S * pow(V,2) * Cx
print("Traînée = "+str(Fx)+" Newtons")

