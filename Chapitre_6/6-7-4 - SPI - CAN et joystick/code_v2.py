""" programme 6-7-4 : orientation joystick avec ADC MCP3008"""
# Importation des librairies natives utiles
from time import *
from board import *
from busio import *
from digitalio import *
# importation de modules supplémentaires
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Instanciation du bus de communication I2C sur le module Feather
bus_spi = SPI(SCK,MOSI,MISO)
# Ajout de la broche (chip select) pour le composant SPI
spi_cs = DigitalInOut(D5)

# Instanciation du convertisseur AN MCP3008
can_mcp3008 = MCP.MCP3008(bus_spi, spi_cs)

# Dictionnaire des directions
directions = {"Nord-Ouest" :(0,1.1,0,1.1), "Nord" :(1.1,2.2,0,1.1), "Nord_Est" :(2.2,3.3,0,1.1),\
            "Ouest" :(0,1.1,1.1,2.2), "Sur place":(1.1,2.2,1.1,2.2), "Est" :(2.2,3.3,1.1,2.2),\
            "Sud_Ouest" :(0,1.1,2.2,3.3), "Sud" :(1.1,2.2,2.2,3.3), "Sud-Est" :(2.2,3.3,2.2,3.3)}
orientation = "Sur place"

while True :
    # Lecture de la tension sur la voie 0 du MCP3308
    joystick_axe_x = AnalogIn(can_mcp3008, MCP.P0).voltage
    # Lecture de la tension sur la voie 1 du MCP3308
    joystick_axe_y = AnalogIn(can_mcp3008, MCP.P1).voltage
    # Recherche de la position du joystick analogique
    for orient,coord in directions.items() :
        if ((coord[0]<=joystick_axe_x<=coord[1]) and (coord[2]<=joystick_axe_y<=coord[3])) :
            orientation = orient
            print (orientation)
    sleep(0.75)
