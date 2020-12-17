"""programme 6-8-3 : Emulation de la souris"""
# importation des modules natifs utiles
from board import *
from digitalio import *
from analogio import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.mouse import Mouse
from simpleio import *

# Instanciation de l'objet 'souris'
souris = Mouse(usb_hid.devices)
# Mise en place des broches des axes du joystick analogique
axe_x = AnalogIn(A4)
axe_y = AnalogIn(A3)
# Mise en place de la broche émulant le bouton gauche de la souris
bouton_gauche = DigitalInOut(A5)
bouton_gauche.direction = Direction.INPUT
bouton_gauche.pull = Pull.UP

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Mesure la valeur numérique des deux axes + mise à l'échelle
    x=map_range(axe_x.value, 0, 65535, 0, 20)
    y=map_range(axe_y.value, 0, 65535, 0, 20)
    # Si le bouton gauche est appuyé alors on émule le clic gauche de la souris
    if bouton_gauche.value is False:
        souris.click(Mouse.LEFT_BUTTON)
    # Si le joystick est à droite, on déplace le curseur d'une unité à droite
    if x > 12.0:
        souris.move(x=1)
    # Si le joystick est à gauche, on déplace le curseur d'une unité à gauche
    if x < 8.0:
        souris.move(x=-1)
    # Si le joystick est vers le haut, on déplace le curseur d'une unité vers le haut
    if y > 12.0:
        souris.move(y=-1)
    # Si le joystick est vers le bas, on déplace le curseur d'une unité vers le bas
    if y < 8.0:
        souris.move(y=1)

