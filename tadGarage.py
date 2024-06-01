#from tadAuto import * //El TAD no usa el otro TAD, son módulos independientes

def crearEst():
    #crear estacionamiento
    return []

def ingresarAuto(estacionamiento, auto):
    #ingresar auto al estacionamiento
    estacionamiento.append(auto)

def eliminarAuto(estacionamiento, a):
    #buscar auto por patente y luego lo elimina de la lista
    estacionamiento.remove(a)

def devolverAuto(estacionamiento, i):
	#devolver un auto pasando como parámetro la posición i-esima en la lista
	return estacionamiento[i]

def tamanioGar(garage):
	#devuelve el tamaño del garage
	return len(garage)
