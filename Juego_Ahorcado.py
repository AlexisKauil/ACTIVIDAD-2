"""Juego del ahorcado"""
"""Alexis Eliseo Kauil Dzib"""

import time
from Clase_Juego import *  #importa los metodos de la clase


jugar=juego()#objeto
print("JUEGO DEL AHORCADO")
time.sleep(4)
palabra = jugar.buscar_palabra() #se seleciona la plabra aleatoria

jugar.adivinar(palabra) #procediemiento para adivinar la palabra



