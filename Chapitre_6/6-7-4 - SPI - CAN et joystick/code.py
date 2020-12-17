""" programme 6-7-4 : liaison SPI avec ADC MCP3008"""
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

while True :
    # Lecture et affichage de la tension sur la voie 0 du MCP3308
    joystick_axe_x = AnalogIn(can_mcp3008, MCP.P0)
    print('valeur numerique axe x : {}'.format(joystick_axe_x.value))
    print('tension axe x : {}'.format(round(joystick_axe_x.voltage,2)) + 'V')
    # Lecture et affichage de la tension sur la voie 1 du MCP3308
    joystick_axe_y = AnalogIn(can_mcp3008, MCP.P1)
    print('valeur numerique axe y : {}'.format(joystick_axe_y.value))
    print('tension axe y : {}'.format(round(joystick_axe_y.voltage,2)) + 'V')
    sleep(0.25)
