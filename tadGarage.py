from tadAuto import *



def crearEst()
    #crear estacionamiento
    return []

def ingresarAuto(estacionamiento, p, hi, t):
    #pide por teclado dato de patente, dueño, hora de entrada y usa crearAuto() para luego ingresarlo al estacionamiento
    a = crearAuto(p, hi , NULL, t)
    estacionamiento.append(a)


def buscarAuto(patente, estacionamiento):
    #usa el valor alfanumérico patente para buscar (recorre la lista)  en un estacionamiento y devuelve la posición en la lista (usa devolverPat(auto) )
    i = 0
    while patente != getPatente(estacionamiento[i]):
            if getpatente(estacionamiento[i]) == NULL:
                break
            else:
                i = i+1
    return i

def eliminarAuto(patente, estacionamiento):
    #buscar auto por patente y luego lo elimina de la lista
    pos = buscarAuto(patente, estacionamiento)
    estacionamiento.pop([pos])


def eliminarBloqueAutos(hora, estacionamiento):
    #elminar todos los elementos de estacionamiento cuya he sea mayor a "hora"
    

