""" programme 6-1-1 :
    commande d'une LED par un bouton poussoir
    A chaque appui, la LED change d'état """
# Importation des librairies natives utiles
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Instanciation de la LED (D13 correspond à la LED intégrée sur le module)
Led = DigitalInOut(board.D13)
Led.direction = Direction.OUTPUT

# Instanciation du bouton (SWITCH correspond au bouton intégré sur le module)
switch = DigitalInOut(board.SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Teste l'état du bouton
    if switch.value == False :
        # S'il est appuyé, on change l'état de la LED
        Led.value = not Led.value
        # Attente pour anti-rebond
        #time.sleep(0.1)
