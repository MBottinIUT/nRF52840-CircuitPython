"""CLUE : éclairage BLE"""
# importation des modules natifs utiles
from board import *
from displayio import *
# importation de modules supplémentaires
import neopixel
from adafruit_display_shapes.triangle import Triangle
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket

# Mise ne place des services Bluetooth BLE
ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# Instanciation de l'écran
ecran = DISPLAY

# Mise en place et affichage du groupe principal (4 objets max)
groupe_principal = Group(max_size=4)
ecran.show(groupe_principal)

# Mise en place de l'image de fond dans le groupe_principal
fichier = open("/images/Fond_Lampe.bmp", "rb")
page = OnDiskBitmap(fichier)
tuile_image = TileGrid(page, pixel_shader=ColorConverter(),x=0,y=0)
groupe_principal.append(tuile_image)

# Mise en place de l'image du logo Bluetooth en Mode déconnecté (visible)
groupe_BT_deconnecte = Group(max_size=1)
fichier = open("/images/Logo_BT_gris.bmp", "rb")
page = OnDiskBitmap(fichier)
tuile_image = TileGrid(page, pixel_shader=ColorConverter(),x=214,y=6)
groupe_BT_deconnecte.append(tuile_image)
groupe_principal.append(groupe_BT_deconnecte)

# Mise en place de l'image du logo Bluetooth en Mode connecté (caché)
groupe_BT_connecte = Group(max_size=1)
fichier = open("/images/Logo_BT_bleu.bmp", "rb")
page = OnDiskBitmap(fichier)
tuile_image = TileGrid(page, pixel_shader=ColorConverter(),x=214,y=6)
groupe_BT_connecte.append(tuile_image)
groupe_principal.append(groupe_BT_connecte)
groupe_principal[2].hidden = True

# Mise en place d'un groupe qui correspond au faisceau de la lampe
groupe_faisceau = Group(max_size = 3)
faisceau_lampe1 = Triangle(64, 53, 136, 126, 0, 71, fill=0x000000, outline=None)
groupe_faisceau.append(faisceau_lampe1)
faisceau_lampe2 = Triangle(136, 126, 72, 239, 0, 71, fill=0x000000, outline=None)
groupe_faisceau.append(faisceau_lampe2)
faisceau_lampe3 = Triangle(72, 239, 0, 239, 0, 71, fill=0x00000, outline=None)
groupe_faisceau.append(faisceau_lampe3)
groupe_principal.append(groupe_faisceau)

# Instanciation de la matrice de 64 LED Neopixels
eclairage = neopixel.NeoPixel(D8, 64, brightness=0.8)

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # La carte CLUE s'annonce via des paquets d'advertising
    ble.start_advertising(advertisement)
    # Et elle le fait tant qu'elle n'est pas connectée
    while not ble.connected:
        pass
    # Dès qu'elle est connectée, elle arrête l'émission de ces paquets
    ble.stop_advertising()
    # On affiche dans ce cas le logo Bluetooth en bleu (connecté)
    groupe_principal[1].hidden = True
    groupe_principal[2].hidden = False
    # boucle sans fin tant que l'on reste connecté
    while ble.connected:
        # Récupération d'un paquet depuis le téléphone
        paquet = Packet.from_stream(uart_server)
        # Si ce paquet correspond à une couleur
        if isinstance(paquet, ColorPacket):
            #print(packet.color)
            # On affiche cette couleur sur la matrice Neopixel
            eclairage.fill(paquet.color)
            # On change la couleur du faisceau de la lampe sur l'écran CLUE
            faisceau_lampe1.fill=paquet.color
            faisceau_lampe2.fill=paquet.color
            faisceau_lampe3.fill=paquet.color
