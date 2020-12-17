""" programme 6-1-1 :
    commande d'une LED par un bouton poussoir
    A chaque appui, la LED change d'état """
# Importation des librairies natives utiles
from time import *
from board import *
from digitalio import *

# Instanciation de la LED (D13 correspond à la LED intégrée sur le module)
Led = DigitalInOut(D13)
Led.direction = Direction.OUTPUT

# Instanciation du bouton (SWITCH correspond au bouton intégré sur le module)
Bouton = DigitalInOut(SWITCH)
Bouton.direction = Direction.INPUT
Bouton.pull = Pull.UP

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Teste l'état du bouton
    if Bouton.value == False :
        # S'il est appuyé, on change l'état de la LED
        Led.value = not Led.value
        # Attente pour anti-rebond
        sleep(0.25)
