"""programme 6-8-3 : tracé automatique dans un logiciel de dessin"""
# importation des modules natives utiles
from time import *
from math import *
# importation de modules supplémentaires
import usb_hid
from adafruit_hid.mouse import Mouse

# Attente pour laisser le temps de se positionner dans la zone de dessin
sleep(5)

# Instanciation de l'objet 'souris'
souris = Mouse(usb_hid.devices)

# constantes définissant la taille des lettres
H = 15
L = 10
E = 10

# Tuple contenant l'ensemble des coordonnées du dessin à effectuer
dessin=((0,2*H,'C'),(2*L,0,'C'),(-2*L,0,'C'),(0,-H,'C'),(2*L,0,'C'),(-2*L,0,'C'),(0,-H,'C'),(2*L,0,'C'),(E,0,'R'),\
        (0,2*H,'C'),(2*L,0,'C'),(E,0,'R'),\
        (2*L,0,'C'),(-2*L,0,'C'),(0,-H,'C'),(2*L,0,'C'),(-2*L,0,'C'),(0,-H,'C'),(2*L,0,'C'),(E,0,'R'),\
        (0,2*H,'C'),(0,-H,'C'),(2*L,-H,'C'),(-2*L,H,'C'),(2*L,H,'C'),(E,-2*H,'R'),\
        (2*L,0,'C'),(-L,0,'C'),(0,2*H,'C'),(E,-2*H,'R'),\
        (2*L,0,'C'),(0,2*H,'C'),(-2*L,0,'C'),(0,-2*H,'C'),(E+2*L,0,'R'),\
        (0,2*H,'C'),(0,-H,'C'),(2*L,H,'C'),(-2*L,-H,'C'),(2*L,0,'C'),(0,-H,'C'),(-2*L,0,'C'))\

# Fonction permettant de déplacer le curseur sur de nouvelles coordonnées en cliquant gauche ou pas
def trace(Depl_X,Depl_Y,BOUTON) :
    # Si le 3ème paramètre est 'C' alors on émule un clic sur le bouton gauche de la souris
    # sinon on relâche l'ensemble des boutons
    if (BOUTON == 'C') :
        souris.press(Mouse.LEFT_BUTTON)
    else :
        souris.release_all()
    # On déplace le curseur via les déplacements relatifs Depl_X et Depl_Y
    souris.move(x=Depl_X, y=Depl_Y)

# On trace le dessin en prenant chaque coordonnée dans le tuple
for coordonnee in dessin :
    trace(coordonnee[0],coordonnee[1],coordonnee[2])
    # pause pour donner l'impression d'un dessin fait à la main
    sleep(0.1)

# Relâche le bouton de la souris et ramène le curseur à gauche sous le dessin précédent
souris.release_all()
souris.move(x=-((6*L)+(5*E)),y=2*H)
# Emule l'appui sur le bouton gauche de la souris puis trace un sinus pour souligner
souris.press(Mouse.LEFT_BUTTON)
for i in range (2*180) :
    souris.move(x=1, y=int(10*sin(i)))

# Emule le relâchement de tous les boutons de la souris
souris.release_all()

print("fin")
