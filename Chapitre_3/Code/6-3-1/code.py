"""programme de jeu de dés"""
# importation des bibliothèques utiles
import random
import time

print ("Jeu de des")
# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True :
	try :
		# Determination des deux lancers
		joueur = random.randint(1,6)
		print ('Votre lancer : {}'.format(joueur))
		feather = random.randint(1,6)
		print ('Au tour de la carte Feather...')
		time.sleep(2)
		print ('Le lancer de la Feather : {}'.format(feather))
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
