""" programme 6-5-3 :
    commande d'une LED par un bouton poussoir
    A chaque appui, la LED change d'état """
# Importation des librairies natives utiles
from time import *
from board import *
from digitalio import *
# importation de modules supplémentaires
from adafruit_debouncer import *

# Instanciation de la LED (D13 correspond à la LED intégrée sur le module)
Led = DigitalInOut(D13)
Led.direction = Direction.OUTPUT

# Instanciation du bouton (SWITCH correspond au bouton intégré sur le module)
Bouton = DigitalInOut(SWITCH)
Bouton.direction = Direction.INPUT
Bouton.pull = Pull.UP
# Ajout de l'anti-rebond
Bouton_avec_antirebond = Debouncer(Bouton)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Mise à jour de la surveillance du bouton
    Bouton_avec_antirebond.update()
    # Teste si un front descendant s'est produit, c'est-à-dire que l'on a appuyé
    # sur le bouton
    if Bouton_avec_antirebond.fell :
        # Dans ce cas, on change l'état de la LED
        Led.value = not Led.value
