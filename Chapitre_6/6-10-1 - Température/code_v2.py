"""programme 6-10-1 : Capteur SHT30 avec module perso"""
# importation des modules natifs utiles
from time import *
from board import *
from busio import *
# importation de modules supplémentaires
import sht30_perso

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C(SCL,SDA)

# Réservation du bus I2C pour le programme
while not bus_i2c.try_lock() :
    pass

# Instanciation du capteur SHT30
capteur_SHT30 = sht30_perso.SHT30(bus_i2c)

sleep(0.5)

# Récupération des informations du capteur
(Temperature_Celcius, Humidite) = capteur_SHT30.lecture()
# Affichage des informations dans la console
print("Temperature : {} C".format(round(Temperature_Celcius,2)))
print("Humidite : {} %".format(round(Humidite,2)))

