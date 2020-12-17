""" Programme 6-5-4 commande d'un servomoteur v2"""
# Importation des librairies natives utiles
from time import *
from board import *
from analogio import *
from pulseio import *
# importation de modules supplémentaires
from simpleio import *

# Instanciation d'une broche analogique
potentiometre = AnalogIn(A1)
# Instanciation d'un signal PWM sur la broche de la LED interne (D13)
led = PWMOut(D13, frequency=5000, duty_cycle=0)
# Instanciation d'un signal PWM pour contrôler un servomoteur sur la broche A2
servomoteur = PWMOut(A2, duty_cycle=4915, frequency=50)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Affichage de la valeur convertie brute du potentiomètre
    print("valeur potentiometre : {}".format(potentiometre.value))
    # Recopie cette valeur vers le rapport cyclique d'un signal PWM
    led.duty_cycle = potentiometre.value
    # Ajuste la valeur du potentiomètre à la plage d'angle du servomoteur
    servomoteur.duty_cycle = int(map_range(potentiometre.value, 0, 65535, 1638, 8192))
    # Attente de 50ms
    sleep(0.05)