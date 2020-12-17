"""programme 6-6-4 : niveau sonore sur LED Neopixel"""
# importation des modules natives utiles
from time import *
from board import *
from pulseio import *
from audiobusio import *
from array import *
from math import *
# importation de modules supplémentaires
from neopixel import *

# Instanciation du microphone (fréquence d'échantillonnage 16kHz / résolution 16 bits)
microphone = PDMIn(MICROPHONE_CLOCK, MICROPHONE_DATA, sample_rate=16000, bit_depth=16)
# Instanciation de la LED neopixel interne
led = NeoPixel(NEOPIXEL, 1)

# Fonction de calcul de la valeur RMS d'une suite d'échantillons audio
def valeur_rms(valeurs):
    # Calcul de la valeur moyenne des échantillons
    moyenne = int(sum(valeurs) / len(valeurs))
    # Calcul et retour de la valeur RMS du signal recentré sur sa valeur moyenne
    return int(sqrt(sum(float(echantillon - moyenne) * (echantillon - moyenne)
                              for echantillon in valeurs) / len(valeurs)))

# ---------------------------------------
# -------  BOUCLE PRINCIPALE  -----------
# ---------------------------------------
while True:
    # Création d'une table de 160 échantillons audio vierge
    echantillons_audio = array('H', [0] * 160)
    # Enregistrement audio de 160 échantillons
    microphone.record(echantillons_audio, len(echantillons_audio))
    # AFfichage des infos des deux capteurs dans la console
    print("\nFeather Sense :")
    print("-----------------")
    niveau_rms = valeur_rms(echantillons_audio)
    print("Niveau sonore (0-65535) :", niveau_rms)
    # Adapte la luminosité de la LED au niveau sonore
    led[0] = (niveau_rms//257,0,0)
    # pause de 50ms
    sleep(0.05)

