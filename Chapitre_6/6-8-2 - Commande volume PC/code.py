"""programme 6-8-2 : Commande de volume"""
# importation des modules natifs utiles
from time import *
from board import *
from digitalio import *
from rotaryio import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Instanciation de la commande multimédia
volume = ConsumerControl(usb_hid.devices)

# Instanciation de l'encodeur en quadrature
encodeur = IncrementalEncoder(D10, D9)

derniere_position = encodeur.position

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Récupération de la position de l'encodeur
    position_actuelle = encodeur.position
    # Contrôle si la position a changé depuis la dernière itération
    changement_position = position_actuelle - derniere_position
    # S'il y a eu une augmentation de x incréments
    if changement_position > 0:
        # On envoie la commande d'augmentation du volume x fois
        for x in range(changement_position):
            volume.send(ConsumerControlCode.VOLUME_INCREMENT)
        print(position_actuelle)
    # ou s'il y a eu une diminution de x incréments
    elif changement_position < 0:
        # On envoie la commande de diminution du volume x fois
        for x in range(-changement_position):
            volume.send(ConsumerControlCode.VOLUME_DECREMENT)
        print(position_actuelle)
    derniere_position = position_actuelle
    # pause de 25ms
    sleep(0.025)
