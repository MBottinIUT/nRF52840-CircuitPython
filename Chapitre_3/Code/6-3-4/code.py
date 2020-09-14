""" Programme sinusoïde"""
# importation des bibliothèques utiles
import math
import time

# Affichage d'une sinusoïde
for i in range (0, 200) :
    # Envoi d'un point
    print((math.sin(i*(math.pi/50)),))
    time.sleep(0.1) 
   