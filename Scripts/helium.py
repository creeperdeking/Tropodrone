

tempc = float(input("temperature:"))
temp = tempc + 273.15

# Constante calculé avec V/T
fpn = 22.414 / 273.25
print("fpn: %f" % fpn)

vol = fpn * temp
vol20 = fpn * (273.15 + 20)
rapport = vol20 / vol

print("volume à 20: %f, volume à %f: %f, rapport de volume: %f" % (vol20, tempc, vol, rapport))

# On calcule les poids
poidair = 1.29 * 9.81
poidhelium = 0.1785 * 9.81
poidheliumtemp = poidhelium * rapport

# Force ascensionnelle: poid air - poid helium
forceasc = poidair - poidhelium
forceasctemp = poidair - poidheliumtemp
rapportforce = forceasctemp / forceasc

print("poids air: %f, poids helium: %f" % (poidair, poidhelium))
print("poids helium à %f: %f" % (tempc, poidhelium * rapport))
print("force ascensionnelle: %f, force ascensionnelle à %f: %f, rapport de force: %f" % (forceasc, tempc, forceasctemp, rapportforce))
