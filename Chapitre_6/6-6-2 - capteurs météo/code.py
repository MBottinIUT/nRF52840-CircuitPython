"""programme 6-6-2 : température/humidité/pression"""
# importation des modules natives utiles
from board import *
# importation de modules supplémentaires
from adafruit_bmp280 import *
from adafruit_sht31d import *

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C()
# Instanciation des deux capteurs qui nous intéressent (connectés sur le bus I2C)
capteur_bmp280 = Adafruit_BMP280_I2C(bus_i2c)
capteur_sht30 = SHT31D(bus_i2c)

# Fixe la valeur de la pression atmosphérique actuelle (hPa) au niveau de la mer
#             --> nécessaire pour le calcul de l'altitude
capteur_bmp280.sea_level_pressure = 1015

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # AFfichage des infos des deux capteurs dans la console
    print("\nFeather Sense : donnees environnementales")
    print("---------------------------------------------")
    print("BMP280 :")
    print("Temperature : {:.1f} C".format(capteur_bmp280.temperature))
    print("pression atmospherique :", capteur_bmp280.pressure)
    print("Altitude : {:.1f} m".format(capteur_bmp280.altitude))
    print("SHT30 :")
    print("Humidite : {:.1f} %".format(capteur_sht30.relative_humidity))
    print("Temperature : {:.1f} C".format(capteur_sht30.temperature))
    # Attente d'un appui sur la touche 'ENTREE'
    input("\nAttente de l'appui sur ENTREE")

