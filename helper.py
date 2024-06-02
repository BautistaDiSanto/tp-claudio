from tadGarage import *
from tadAuto import *


def buscarAuto(estacionamiento, patente):
	j = 0   #posición en estacionamiento
	while j < tamanioGar(estacionamiento):          #voy recorriendo todo el est
		#print(j)
		a = devolverAuto(estacionamiento, j)
		#si es True tengo que quedarme con ese auto y cortar el bucle
		#print(j)
		if (getPatente(a) == patente):
			return j
			break
		j = j +1

