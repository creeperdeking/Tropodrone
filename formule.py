import math

def calculsDrone():
	cout_surface = 1

nbBallon = int(input("Nombre de ballons de même contenance: "))

volume = float(input("Donnez le volume de votre/vos ballon(s) (m^3): "))/nbBallon

print("Volume par ballons: ", volume)
print("\n")
masses = [147, #Structure
	  4*18, # Moteurs
	  4*9, #ESC - permet de controller le courant
	  2*4, #Helices
	  184, #Batterie
	  9, #Microcontrolleur
	  25, #Cablages
	  ]

coutsCsttes = [80, #drone
	20, #batterie
	50, #estimation cout helium
	28 #Frais de ports
	]

while True:
	ans = input("Donnez la largeur de votre ballon (cm): ")
	if ans == "stop":
		break

	rayon = float(ans)/2
	print("Rayon du ballon: ", rayon)
	print("\n\n")
	hauteur = (volume/(math.pi*(pow(rayon/100,2))))*100
	print("Longueur d'un ballon: ", round(hauteur, 2), "cm")
	aire = (2*math.pi*rayon*hauteur + math.pi*pow(rayon, 2)*2)*nbBallon
	print("Surface de tissus nécessaire totale: ", round(aire/10000, 2), "m^2")

	print("Masse et portance: ")
	masseBallons = 17 * aire/10000 #Masse, en grammes par m²
	cout = cout_surface * aire/10000 #Cout au m²
	coutTotal = 0
	for i in coutsCsttes:
		coutTotal += i
	coutTotal += cout
	masseTotale = 0
	for i in masses:
		masseTotale += i
	masseTotale+= masseBallons

	#calculs de structure:
	#structureExterne:
	coutStructure = 2 #€/m
	longueurCarbonne = 3*2*hauteur+ 2 #On rajoute 2 pour faire une estimation haute
	epaisseurCarbonne = 0.2
	MVCarbonne = .3 #Masse volumique du carbonne (g/cm)
	masseCarbonne = longueurCarbonne * MVCarbonne
	#structureCerclesCentraux:
	coutCercles = 2 #€/m
	separationArceaux = 3
	longueurDefaut = 0.3273502692
	distanceArbitraire = 5
	epaisseurCercles = 0.2
	MVCercles = 5/1000 #Masse Centimetrique des cercles (g/cm)
	perimetresCercles = [0,0,0]
	for i in range(0,2):
		perimetresCercles[i] = (longueurDefaut*hauteur-distanceArbitraire-separationArceaux*i*2)*2*math.pi
	longueurCercles = (perimetresCercles[0] + perimetresCercles[1] + perimetresCercles[2])
	masseCercles = longueurCercles * epaisseurCercles*math.pi*MVCercles

	coutTotal += coutCercles*longueurCercles/100 + coutStructure*longueurCarbonne/100
	masseTotale += masseCercles + 50 + masseCarbonne
	print("Masse ballons: ", round(masseBallons, 2), "g")
	print("Masse totale: ", round(masseTotale, 2), "g")
	print("Cout ballons: ", round(cout, 2), "€")
	print("Cout total: ", round(coutTotal, 2), "€")

def permeabilite():
	epaisseur = 0
	pression = 1
	temperature = 0
	print("Quel est l'epaissseur de mylar? (µm)")
	input(epaisseur)
	print("Quelle température? (C° Celcius)")
	input(temperature)


def main():
	print("Quel calcul:")
	print("    1: Calculs généraux sur le drone")
	print("    2: Calculs de perméabilité")
	reponse = ""
	input(reponse)
	if reponse == "1":
		calculsDrone()
	elif reponse == "2":
		premeabilite()
	print("\n\n")

main()
