"""programme 6-7-2 : Test de la liaison série UART"""
# importation des modules natives utiles
from time import *
from board import *
import busio
# importation de modules supplémentaires
from adafruit_apds9960.apds9960 import *
from adafruit_bmp280 import *
from adafruit_lis3mdl import *
from adafruit_lsm6ds import *
from adafruit_sht31d import *

# Instanciation du bus de communication UART sur le module Feather
uart = busio.UART(TX, RX, baudrate=9600)
# Instanciation du bus de communication I2C sur le module Feather
i2c = I2C()
# Instanciation des différents capteurs
capteur_apds9960 = APDS9960(i2c)
capteur_bmp280 = Adafruit_BMP280_I2C(i2c)
capteur_lis3mdl = LIS3MDL(i2c)
capteur_lsm6ds33 = LSM6DS33(i2c)
capteur_sht31d = SHT31D(i2c)

# Autorisation du mode de détection de couleurs pour le capteur APDS-9960
capteur_apds9960.enable_proximity = True
capteur_apds9960.enable_color = True

# Envoi vers le PC des messages pour l'utilisateur
uart.write(bytearray(b'Quelle grandeur vous interesse ?\n'))
uart.write(bytearray(b'T - temperature\n'))
uart.write(bytearray(b'P - pression\n'))
uart.write(bytearray(b'H - humidite\n'))
uart.write(bytearray(b'O - orientation\n'))
uart.write(bytearray(b'C - couleur\n'))
uart.write(bytearray(b'\n'))

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
	# Lecture depuis le PC de 2 octets
    donnee = uart.read(2)
    # Teste si l'on a effectivement reçu quelque chose envoyé par l'utilisateur
    if donnee != b'' :
        # Création d'une chaîne de caractères à partir de la donnée reçue
		donnee_chaine = ''.join([chr(b) for b in donnee])
		# Test de la donnee reçue et création de la chaîne réponse associée
        if donnee_chaine[0] == 'T' :
            reponse = "Temperature : {:.1f} C".format(capteur_bmp280.temperature)
        elif donnee_chaine[0] == 'P' :
            reponse = "Pression : {}".format(capteur_bmp280.pressure)
        elif donnee_chaine[0] == 'H' :
            reponse = "Humidite: {:.1f} %".format(capteur_sht31d.relative_humidity)
        elif donnee_chaine[0] == 'O' :
            reponse = "Acceleration: {:.2f} {:.2f} {:.2f} m/s^2" \
										.format(*capteur_lsm6ds33.acceleration)
        elif donnee_chaine[0] == 'C' :
            reponse = "R: {}, G: {}, B: {}, C: {}" \ 
										.format(*capteur_apds9960.color_data)
		# Envoi de la réponse vers le PC
        uart.write(bytearray(reponse))
		# Envoi vers le PC des messages pour l'utilisateur
        uart.write(bytearray(b'\n'))
        uart.write(bytearray(b'\n'))
        uart.write(bytearray(b'Quelle grandeur vous interesse ?\n'))
        uart.write(bytearray(b'T - temperature\n'))
        uart.write(bytearray(b'P - pression\n'))
        uart.write(bytearray(b'H - humidite\n'))
        uart.write(bytearray(b'O - orientation\n'))
        uart.write(bytearray(b'C - couleur\n'))
        uart.write(bytearray(b'\n'))
    sleep(0.5)

