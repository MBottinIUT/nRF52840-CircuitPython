""" programme 6-1-2 :
    commande d'une LED par un bouton poussoir
    A chaque appui, la LED change d'état """
# Importation des librairies natives utiles
from time import *
from board import *
from digitalio import *

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
    # Teste l'état du bouton
    if Bouton.value == False :
        # S'il est appuyé, on change l'état de la LED
        Led.value = not Led.value
        # Attente pour anti-rebond
        sleep(0.25)
