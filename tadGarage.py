#from tadAuto import * //El TAD no usa el otro TAD, son módulos independientes

def crearEst():
    #crear estacionamiento
    return []

def ingresarAuto(estacionamiento, auto): #patente, horaIngreso, horaEgreso, monto, torre):
    #auto = createCar(patente, horaIngreso, horaEgreso, monto, torre)
    #print("agregando auto") 	//Las funciones del TAD no llevan prints
    estacionamiento.append(auto)


"""def buscarAuto(patente, estacionamiento):
    #usa el valor alfanumérico patente para buscar (recorre la lista)  en un estacionamiento y devuelve la posición en la lista (usa devolverPat(auto) )
    i = 0
    while patente != getPatente(estacionamiento[i]):
            if getpatente(estacionamiento[i]) == NULL:
                break
            else:
                i = i+1
    return i"""

def eliminarAuto(estacionamiento, a):
    #buscar auto por patente y luego lo elimina de la lista
    	#pos = buscarAuto(patente, estacionamiento)
    estacionamiento.remove(a)


"""def eliminarBloqueAutos(hora, estacionamiento):
    #elminar todos los elementos de estacionamiento cuya he sea mayor a "hora"
"""

def devolverAuto(estacionamiento, i):
	#devolver un auto pasando como parámetro la posición i-esima en la lista
	return estacionamiento[i]

def tamanioGar(garage):
	#devuelve el tamaño del garage
	return len(garage)
