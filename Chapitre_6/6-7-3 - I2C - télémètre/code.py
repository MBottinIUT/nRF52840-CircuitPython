"""programme 6-7-3 : télémètre ToF I2C VL6180X"""
# importation des modules natives utiles
from time import *
from board import *
from busio import *
# importation de modules supplémentaires
from adafruit_vl6180x import *

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C(SCL, SDA)

# Instanciation du telemetre VL6180X
telemetre_ToF = VL6180X(bus_i2c)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Lecture de la distance de l'obstacle et son affichage
    distance_mm = telemetre_ToF.range
    print("Distance: {} mm".format(distance_mm))
    sleep(1.0)
