"""programme 6-10-1 : Capteur SHT30"""
# importation des modules natifs utiles
from time import *
from board import *
from digitalio import *
from busio import *
# importation de modules supplémentaires

# Instanciation du bus de communication I2C sur le module Feather
bus_i2c = I2C(SCL,SDA)

# Réservation du bus I2C pour le programme
while not bus_i2c.try_lock() :
    pass

# Adresse I2C du capteur SHT30
adresse_i2c_sht30 = 0x44

# Configuration du SHT30 pour une vitesse de mesure élevée
bus_i2c.writeto(adresse_i2c_sht30,bytes([0x2C, 0x06]))

sleep(0.5)

# Lecture de 6 octets de données
donnees = bytearray(6)
bus_i2c.readfrom_into(adresse_i2c_sht30, donnees)

# Calcul de la température en Celcius
Temperature_Celcius = ((((donnees[0] * 256.0) + donnees[1]) * 175) / 65535.0) - 45
# Calcul du taux d'humidité
Humidite = 100 * (donnees[3] * 256 + donnees[4]) / 65535.0
# Affichage des informations dans la console
print("Temperature : {} C".format(round(Temperature_Celcius,2)))
print("Humidite : {} %".format(round(Humidite,2)))

