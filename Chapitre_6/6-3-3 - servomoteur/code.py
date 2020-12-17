""" Programme 6-3-3 commande d'un servomoteur """
# Importation des librairies natives utiles
from time import *
from board import *
from analogio import *
from pulseio import *

# Instanciation d'une broche analogique
potentiometre = AnalogIn(A1)
# Instanciation d'un signal PWM sur la broche de la LED interne (D13)
led = PWMOut(D13, frequency=5000, duty_cycle=0)
# Instanciation d'un signal PWM pour contrôler un servomoteur sur la broche A2
# Servomoteur : impulsion de 1ms à 2ms sur un signal de 20ms (50Hz)
#               soit rapport cyclique temporel de 5% à 10%
#               soit son équivalent en numérique : de 3277 à 6553
# exemple servomoteur au centre de sa course : impulsion de 1,5ms --> rapport cyclique de 4915
servomoteur = PWMOut(A2, duty_cycle=4915, frequency=50)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Affichage de la valeur convertie brute du potentiomètre
    print("valeur potentiometre : {}".format(potentiometre.value))
    # Recopie cette valeur vers le rapport cyclique d'un signal PWM
    led.duty_cycle = potentiometre.value
    # Ajuste la valeur du potentiomètre à la plage de rapport cyclique du servomoteur
    servomoteur.duty_cycle = int((potentiometre.value / 20) +3277)
    # Attente de 50ms
    sleep(0.05)

