"""programme 6-8-2 : commande d'un diaporama sur PC par gestes"""
# importation des modules natifs utiles
from time import *
from board import *
from digitalio import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import *

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C()

# Instanciation du capteur de gestes APDS-9960
capteur_apds9960 = APDS9960(bus_i2c)
capteur_apds9960.enable_proximity = True
capteur_apds9960.enable_gesture = True

# Instanciation du clavier
clavier = Keyboard(usb_hid.devices)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Récupère la détection de gestes
    gestes = capteur_apds9960.gesture()
    # Teste si un balayage gauche ou un balayage droit s'est produit
    if gestes == 0x03:
        print("balayage gauche")
        # On envoie le code clavier de la flèche gauche
        clavier.send(Keycode.LEFT_ARROW)
    elif gestes == 0x04:
        print("balayage droit")
        # On envoie le code clavier de la flèche droite
        clavier.send(Keycode.RIGHT_ARROW)
    # pause de 100ms
    sleep(0.1)
