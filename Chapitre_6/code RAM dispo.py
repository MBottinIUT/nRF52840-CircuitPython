""" Test de la mémoire RAM disponible """
# Importation des librairies natives utiles
#from time import *
from time import sleep
from gc import *

sleep(0.5)
print ("memoire allouee : {}".format(mem_alloc()))
print ("memoire disponible : {}".format(mem_free()))
