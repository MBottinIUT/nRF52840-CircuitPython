"""programme 6-8-2 : Jeu Chrome T-Rex"""
# importation des modules natifs utiles
from time import *
from board import *
from digitalio import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import *

# Instanciation du clavier
clavier = Keyboard(usb_hid.devices)

# Instanciation du bouton de commande
Bouton = DigitalInOut(D2)
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
    # Teste si un front descendant s'est produit,
    # c'est-à-dire que l'on a appuyé sur le bouton
    if Bouton_avec_antirebond.fell :
        # Dans ce cas, on envoie le code de la barre d'espace
        clavier.send(Keycode.SPACE)
    # pause de 25ms
    sleep(0.025)

