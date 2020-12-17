""" Programme 6-2-1 mesure de la tension d'un potentiomètre """
# Importation des librairies natives utiles
from time import *
from board import *
from analogio import *

# Instanciation d'une broche analogique
potentiometre = AnalogIn(A1)

# Fonction de calcul de la tension sur la broche analogique spécifiée
def mesure_tension(broche):
    return (broche.value * 3.3) / 65536

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    print("Tension : {} Volt(s)".format(round(mesure_tension(potentiometre),2)))
    # Attente avant la mesure suivante
    sleep(0.75)
