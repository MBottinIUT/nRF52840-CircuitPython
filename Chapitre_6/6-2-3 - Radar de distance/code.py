""" Programme 6-3-2 variation de l'intensité lumineuse d'une LED """
# Importation des librairies natives utiles
from time import *
from board import *
from analogio import *
from pulseio import *

# Instanciation d'une broche analogique
capteur = AnalogIn(A1)

# Fonction de calcul de la tension sur la broche analogique
def mesure_tension(broche) :
    return (broche.value *3.3)/65536

# Fonction de détermination de la distance de l'obstacle
def calcul_distance(tension) :
    return ((13 - (0.42*tension))/tension)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    print(mesure_tension(capteur))
    distance = round(calcul_distance(mesure_tension(capteur)),1)
    if (distance >= 30.0) :
        distance = 30.0
    print("Distance : {} cm(s)".format(distance))
    # Attente de 25ms
    sleep(0.05)

