"""programme de jeu de dés"""
# importation des bibliothèques utiles
import random
import time

print ("Jeu de des")

# Déclaration des dessins des dés
Valeurs_de = {
	"1": [
	" ------- ",
	"|       |",
	"|   o   |",
	"|       |",
	" ------- "
	],
	"2": [
	" ------- ",
	"| o     |",
	"|       |",
	"|     o |",
	" ------- "
	],
	"3": [
	" ------- ",
	"| o     |",
	"|   o   |",
	"|     o |",
	" ------- "
	],
	"4": [
	" ------- ",
	"| o   o |",
	"|       |",
	"| o   o |",
	" ------- "
	],
	"5": [
	" ------- ",
	"| o   o |",
	"|   o   |",
	"| o   o |",
	" ------- "
	],
	"6": [
	" ------- ",
	"| o   o |",
	"| o   o |",
	"| o   o |",
	" ------- "
	]
}

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True :
	try :
		# Determination des deux lancers
		joueur = random.randint(1,6)
		print ('Votre lancer : ')
		for ligne in range(len(Valeurs_de['1'])):
			print(Valeurs_de[str(joueur)][ligne])
		feather = random.randint(1,6)
		print ('Au tour de la carte Feather...')
		time.sleep(2)
		for ligne in range(len(Valeurs_de['1'])):
			print(Valeurs_de[str(feather)][ligne])
		# Determination du gagnant
		if joueur > feather :
			print ('Vous gagnez !!')
		elif joueur < feather :
			print ('Vous perdez !!')
		else :
			print ('Match nul...')
		# Demande pour rejouer
		nouvelle_partie = str(input('Voulez-vous rejouer (o/n) ?'))
		nouvelle_partie = nouvelle_partie.upper()
		if nouvelle_partie != 'O' :
			break
	except KeyboardInterrupt :
		print ("Au revoir...")
		break
