if int(Re) < 1: # Stokes
    Cx = 24 / Re
elif int(Re) < pow(10,3): # Intermediaire
    Cx = 18.5 / pow(Re, 0.6)
elif int(Re) > pow(10,3): # Turbulent
    Cx = 0.44

Fx = 0.5 * P * S * pow(V,2) * Cx
print("Trainee = "+str(Fx)+" Newtons")
