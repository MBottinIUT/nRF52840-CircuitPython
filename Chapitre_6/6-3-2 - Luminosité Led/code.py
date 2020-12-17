""" Programme 6-3-2 variation de l'intensité lumineuse d'une LED """
# Importation des librairies natives utiles
from time import *
from board import *
from analogio import *
from pulseio import *

# Instanciation d'une broche analogique
potentiometre = AnalogIn(A1)
# Instanciation d'un signal PWM sur la broche de la LED interne (D13)
led = PWMOut(D13, frequency=5000, duty_cycle=0)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Affichage de la valeur convertie brute du potentiometre
    print("valeur potentiometre : {}".format(potentiometre.value))
    # Recopie cette valeur vers le rapport cyclique du signal PWM
    led.duty_cycle = potentiometre.value
    # Attente de 50ms
    sleep(0.05)

