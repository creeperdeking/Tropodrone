import math

P = 0.1785 # masse volumique air
S = float(input("Surface du ballon (m^2) = "))
L = float(input("Diametre du ballon (m) = "))
V = float(input("Vitesse relative du fluide (en m.s^-1) = "))

nu = 15.6 * pow(10,-6) # Coeff viscosite cinematique air

Re = (V * L) / nu  # Nombre de reynolds
print("Re = "+str(Re))
