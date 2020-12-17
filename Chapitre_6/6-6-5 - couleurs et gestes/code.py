"""programme 6-6-5 : variation couleur LED par gestes"""
# importation des modules natives utiles
from time import *
from board import *
# importation de modules supplémentaires
from neopixel import *
from adafruit_apds9960.apds9960 import *
from adafruit_fancyled.adafruit_fancyled import *

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C()

# Instanciation de la LED neopixel interne
led = NeoPixel(NEOPIXEL, 1)
# Instanciation du capteur de gestes APDS-9960
capteur_apds9960 = APDS9960(bus_i2c)
capteur_apds9960.enable_proximity = True
capteur_apds9960.enable_gesture = True

# Variables globales
teinte = 0.0
pas = 0.05

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Récupère la détection de gestes
    gestes = capteur_apds9960.gesture()
    # Teste si un balayage gauche ou un balayage droit s'est produit
    # Dans ce cas, modifie la teinte d'un pas (+/-)
    if gestes == 0x03:
        print("balayage gauche")
        teinte = teinte - pas
    elif gestes == 0x04:
        print("balayage droit")
        teinte = teinte + pas
    # Génération de la couleur correspondante à la teinte
    couleur_HSV = CHSV(teinte, 1.0, 1.0)
    # Conversion d e HSV vers RGB
    couleur_RGB = couleur_HSV.pack()
    # Change la teinte de la LED neopixel selon le geste effectué
    led[0] = (couleur_RGB)
    # pause de 10ms
    sleep(0.01)

