"""programme 6-8-2 : saisie dans un tableur"""
# importation des modules natifs utiles
from time import *
from board import *
from digitalio import *
# importation de modules supplémentaires
from adafruit_lsm6ds import *
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Instanciation du clavier
clavier = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(clavier)

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C()
# Instanciation de l'accéléromètre LSM6DS33
accelerometre = LSM6DS33(bus_i2c)

# Instanciation de la LED interne et du bouton interne
led = DigitalInOut(D13)
led.direction = Direction.OUTPUT
led.value = False
bouton = DigitalInOut(SWITCH)
bouton.pull = Pull.UP

# Attente d'appui sur le bouton permettant à l'utilisateur de se placer
# sur la feuille de son tableur
while bouton.value:
    pass
led.value = True
sleep(2)

# Fonction limitant la vitesse d'envoi des caractères pour que le PC suive
def ecriture_lente(chaine):
    for c in chaine:
        layout.write(c)
        sleep(0.2)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
mesure = 1
print("debut des mesures")
# Boucle de 10 mesures
while mesure < 11:
    # Création et envoi au PC de la chaîne 'mesure x' où x est le numéro de
    # la mesure
    chaine_mesure = "mesure {}".format(mesure)
    ecriture_lente(chaine_mesure)
    # Changement de cellule
    clavier.send(Keycode.TAB)
    # mesure et envoi au PC de la valeur de l'accélération sur l'axe X
    valeur_accel_X = str(round(accelerometre.acceleration[0],2))
    print(valeur_accel_X)
    ecriture_lente(valeur_accel_X)
    # Changement de ligne et retour à la première colonne
    clavier.press(Keycode.DOWN_ARROW)
    sleep(0.2)
    clavier.press(Keycode.HOME)
    clavier.release_all()
    # incrémentation du numéro de la mesure
    mesure = mesure +1
    # Attente de 1s
    sleep(1.0)
print("fin des mesures")
led.value = False
