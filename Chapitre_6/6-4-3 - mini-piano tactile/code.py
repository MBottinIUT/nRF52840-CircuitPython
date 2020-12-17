""" Programme 6-4-3 mini-piano tactile """
# Importation des librairies natives utiles
from time import *
from board import *
from touchio import *
from pulseio import *

# Instanciation d'un signal PWM pour le piezo sur la broche A2
piezo = PWMOut(A2, duty_cycle=0, frequency=440, variable_frequency=True)

# Instanciation des boutons tactiles pour chaque note
Touche_do3 = TouchIn(D2)
Touche_re3 = TouchIn(D5)
Touche_mi3 = TouchIn(D6)
Touche_fa3 = TouchIn(D9)
Touche_sol3 = TouchIn(D10)
Touche_la3 = TouchIn(D11)
Touche_si3 = TouchIn(D12)
Touche_do4 = TouchIn(D13)
Touche = True

# Fréquences de la gamme
gamme = {"do3" :262, "re3" :294, "mi3" :330, "fa3" :349, "sol3" :392, "la3" :440, "si3" :494, "do4" :523}

# fonction jouant la note pendant 250ms
def joue_note(note) :
    piezo.frequency = gamme[note]
    piezo.duty_cycle = 65535 // 2
    sleep(0.25)
    piezo.duty_cycle = 0

while True:
    if (Touche_do3.value == Touche) :
        joue_note("do3")
    elif (Touche_re3.value == Touche) :
        joue_note("re3")
    elif (Touche_mi3.value == Touche) :
        joue_note("mi3")
    elif (Touche_fa3.value == Touche) :
        joue_note("fa3")
    elif (Touche_sol3.value == Touche) :
        joue_note("sol3")
    elif (Touche_la3.value == Touche) :
        joue_note("la3")
    elif (Touche_si3.value == Touche) :
        joue_note("si3")
    elif (Touche_do4.value == Touche) :
        joue_note("do4")
