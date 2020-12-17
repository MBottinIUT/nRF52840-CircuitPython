"""programme 6-6-6 : couleur aléatoire LED avec accéléromètre"""
# importation des modules natives utiles
from time import *
from board import *
from random import *
# importation de modules supplémentaires
from neopixel import *
from adafruit_lsm6ds import *
from adafruit_fancyled.adafruit_fancyled import *

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C()

# Instanciation de la LED neopixel interne
led = NeoPixel(NEOPIXEL, 1)
# Instanciation de l'accéléromètre LSM6DS33
accelerometre = LSM6DS33(bus_i2c)

# variables globales
teinte = 0.0
seuil_haut = 6.5
seuil_bas =1.5

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Tant que l'on n'incline pas suffisamment l'accéléromètre, on attend
    while True :
        valeur_accel_Y = abs(accelerometre.acceleration[1])
        print(valeur_accel_Y)
        # teinte aléatoire si valeur accéléromètre dépasse seuil
        if (valeur_accel_Y > seuil_haut) :
            teinte = random()
            break
    # Génération de la couleur correspondante à la teinte
    couleur_HSV = CHSV(teinte, 1.0, 1.0)
    # Conversion d e HSV vers RGB
    couleur_RGB = couleur_HSV.pack()
    # Change la teinte de la LED neopixel selon le geste effectué
    led[0] = (couleur_RGB)
    # Tant que l'on ne ramène pas l'accéléromètre dans sa position horizontale, on attend
    while True :
        valeur_accel_Y = abs(accelerometre.acceleration[1])
        if (valeur_accel_Y < seuil_bas) :
            break
    # Attente de 50ms
    sleep(0.05)
