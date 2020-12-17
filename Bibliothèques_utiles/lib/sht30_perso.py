from board import *
from busio import *

class SHT30(object):

    def __init__(self, bus_i2c):
        self.adresse_i2c_sht30 = 0x44
        self.bus_i2c = bus_i2c
        self.bus_i2c.writeto(self.adresse_i2c_sht30,bytes([0x2C, 0x06]))

    def lecture(self):
        donnees = bytearray(6)
        self.bus_i2c.readfrom_into(self.adresse_i2c_sht30, donnees)
        temperature = ((((donnees[0] * 256.0) + donnees[1]) * 175) / 65535.0) - 45
        humidite = 100 * (donnees[3] * 256 + donnees[4]) / 65535.0
        return (temperature, humidite)
