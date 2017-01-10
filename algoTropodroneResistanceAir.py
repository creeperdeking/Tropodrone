import math

# Portance ou trainee 
print("")
print("")
print("CALCUL DE PORTANCE ET DE TRAÎNÉE")
print("1 - Calcul de portance ")
print("2 - Calcul de traînée ")
choix = int(input("? "))

print("")
print("")

P = 0.1785 # kg/m^3 (masse volumique de l'air)
S = float(input("Surface du ballon (m^2) = "))
V = float(input("Vitesse relative du fluide (en m.s^-1) = "))

if choix == 1:
    Cz = float(input("Cz = "))
    Fz = 0.5 * P * S * pow(V,2) * Cz
    print("Portance = "+str(Fz)+" Newtons")
elif choix == 2:
    Cx = float(input("Cx = "))
    Fx = 0.5 * P * S * pow(V,2) * Cx
    print("Traînée = "+str(Fx)+" Newtons")
