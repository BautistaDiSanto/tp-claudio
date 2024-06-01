from tadGarage import *
from tadAuto import *


def buscarAuto(estacionamiento, patente):
	j = 0   #posición en estacionamiento
	while j < tamanioGar(estacionamiento):          #voy recorriendo todo el est
		a = devolverAuto(estacionamiento, j)
		#si es True tengo que quedarme con ese auto y cortar el bucle
		if (getPatente(a) == patente):
			return j
			break

