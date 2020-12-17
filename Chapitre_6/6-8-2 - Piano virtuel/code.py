"""programme 6-8-2 : Indiana Jones (www.virtualpiano.net)"""
# importation des modules natifs utiles
from time import *
from board import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Instanciation du clavier
clavier = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(clavier)

# Constantes entre notes
PAUSE = 0.3
LONGUE_PAUSE = 0.7

melodie = ['u','i','o','s','$','y','u','i','$','o','p','q','g','$',\
        'p','q','s','d','f','$','u','i','o','s','$',\
        'd','f','g','o','o','f','d','o','f','d','o','f','d','o','f','d','$',
        'u','i','o','s','$','y','u','i','$','o','p','q','g','$',\
        'p','q','s','d','f','$','u','i','o','s','$',\
        'd','f','g','o','o','f','d','o','f','d','o','f','d','o','f','d','$',\
        'u','o','i','y','i','u','o','f','u','o','i','y','i','u','o','f',\
        'd','f','g','d','g','D','d','s','s','d','o','l','o','d','o','l','o',\
        'd','s','a','s','u','o','i','y','i','u','o','f','u','o','i','y','i',\
        'Y','y','t','u','o','i','y','i','u','o','f','d','g','P','p','P','g',\
        'P','p','P','g','D','d','D','s','s','g','P','p','P','g','P','p','P',\
        'g','D','d','D','$','s','g','P','p','P','g','P','p','P','g','D','d',\
        'D','O','o','O','D','O','o','O','D','g','h']

# Pause permettant à l'utilisateur de se placer sur la page www.virtualpiano.net
sleep(5)
# Lecture de chaque élement de la liste 'melodie'
for note in melodie :
    # si l'élément est '$', on fait une pause plus longue
    if note == '$' :
        sleep(LONGUE_PAUSE)
    # sinon on envoie le code de la touche et on marque une courte pause
    else :
        layout.write(note)
        sleep(PAUSE)

