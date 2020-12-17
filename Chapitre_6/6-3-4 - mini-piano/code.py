""" Programme 6-3-4 mini-piano """
# Importation des librairies natives utiles
from time import *
from board import *
from digitalio import *
from pulseio import *

# Instanciation d'un signal PWM pour le piezo sur la broche A2
piezo = PWMOut(A2, duty_cycle=0, frequency=440, variable_frequency=True)

# Instanciation des boutons pour chaque note
Bouton_do3 = DigitalInOut(D2)
Bouton_do3.direction = Direction.INPUT
Bouton_do3.pull = Pull.UP
Bouton_re3 = DigitalInOut(D5)
Bouton_re3.direction = Direction.INPUT
Bouton_re3.pull = Pull.UP
Bouton_mi3 = DigitalInOut(D6)
Bouton_mi3.direction = Direction.INPUT
Bouton_mi3.pull = Pull.UP
Bouton_fa3 = DigitalInOut(D9)
Bouton_fa3.direction = Direction.INPUT
Bouton_fa3.pull = Pull.UP
Bouton_sol3 = DigitalInOut(D10)
Bouton_sol3.direction = Direction.INPUT
Bouton_sol3.pull = Pull.UP
Bouton_la3 = DigitalInOut(D11)
Bouton_la3.direction = Direction.INPUT
Bouton_la3.pull = Pull.UP
Bouton_si3 = DigitalInOut(D12)
Bouton_si3.direction = Direction.INPUT
Bouton_si3.pull = Pull.UP
Bouton_do4 = DigitalInOut(D13)
Bouton_do4.direction = Direction.INPUT
Bouton_do4.pull = Pull.UP

Appuye = False

# Fréquences de la gamme
gamme = {"do3" :262, "re3" :294, "mi3" :330, "fa3" :349, "sol3" :392, "la3" :440, "si3" :494, "do4" :523}

# fonction jouant la note pendant 250ms
def joue_note(note) :
    piezo.frequency = gamme[note]
    piezo.duty_cycle = 65535 // 2
    sleep(0.25)
    piezo.duty_cycle = 0

while True:
    if (Bouton_do3.value == Appuye) :
        joue_note("do3")
    elif (Bouton_re3.value == Appuye) :
        joue_note("re3")
    elif (Bouton_mi3.value == Appuye) :
        joue_note("mi3")
    elif (Bouton_fa3.value == Appuye) :
        joue_note("fa3")
    elif (Bouton_sol3.value == Appuye) :
        joue_note("sol3")
    elif (Bouton_la3.value == Appuye) :
        joue_note("la3")
    elif (Bouton_si3.value == Appuye) :
        joue_note("si3")
    elif (Bouton_do4.value == Appuye) :
        joue_note("do4")
