""" programme 6-1-3 :
    simple testeur de réflexes avec LED et bouton """
# Importation des librairies natives utiles
from time import *
from board import *
from digitalio import *
from random import *

# Instanciation de la LED
Led = DigitalInOut(D5)
Led.direction = Direction.OUTPUT

# Instanciation du bouton
Bouton = DigitalInOut(A5)
Bouton.direction = Direction.INPUT
Bouton.pull = Pull.UP

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    Led.value = True        # Allume la LED
    print ("Appuyez sur le bouton lorsque la LED s'eteint...")
    sleep(randint(1,10))        # Attente aléatoire
    instant_debut = monotonic_ns()     # enregistre le temps actuel
    Led.value = False       # Eteint la LED
    while Bouton.value == True :        # Attente que l'on appuie sur le bouton
        pass
    instant_fin = monotonic_ns()       # enregistre le temps actuel
    # Affiche la différence entre les deux enregistrements de temps
    print ("Vous avez reagi en {} secondes".format((instant_fin-instant_debut)/1e9))
    sleep(4)        # Attente avant de recommencer
