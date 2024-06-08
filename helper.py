from tadGarage import *
from tadAuto import *
from tadCola import *
import datetime

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
          
def deltaHoras(ingreso, egreso):
    diferencia = egreso - ingreso
    segundos = diferencia.total_seconds()
    horas = segundos * 1/3600
    return horas

def updateAutosPico(horaIngreso, autosPico):
    if int(horaIngreso.hour) >= 7 and int(horaIngreso.hour) <= 10:
        if int(horaIngreso.hour) < 10:
            autosPico[0] += 1
        elif int(horaIngreso.hour) == 10 and int(horaIngreso.minute) == 0:
            autosPico[0] += 1

    if int(horaIngreso.hour) >= 17 and int(horaIngreso.hour) <= 20:
        if int(horaIngreso.hour) < 20:
            autosPico[0] += 1
        elif int(horaIngreso.hour) == 20 and int(horaIngreso.minute) == 0:
            autosPico[0] += 1

def load_vehicles_from_file(filename, estacionamiento, registro, valorHora, autosPico):
    try:
        with open(filename, 'r') as file:
            n = 0
            lines = file.readlines()
            for line in lines:
                n += 1
                data = line.strip().split(', ')
                if len(data) != 4:
                    print(f"Invalid line format: {line}")
                    continue
                
                patente = data[0].strip()
                horaIngreso = datetime.datetime.strptime(data[1].strip(), '%H:%M')
                updateAutosPico(horaIngreso, autosPico)
                torre = int(data[3].strip())

                if data[2].strip() == "null":
                    auto = createCar()
                    fillCar(auto, patente, horaIngreso, None, None, torre)
                    ingresarAuto(estacionamiento, auto)
                else:
                    horaEgreso = datetime.datetime.strptime(data[2].strip(), '%H:%M')
                    descuento = 1
                    #si pertenece a la torre 3 descontar 15% ( x 0,85)
                    if torre == 3:
                        descuento = 0.85
                    monto = (deltaHoras(horaIngreso, horaEgreso) * valorHora) * descuento
                    auto = createCar()
                    fillCar(auto, patente, horaIngreso, horaEgreso, monto, torre)
                    ingresarAuto(registro, auto)

                print("")
                print(f"Vehicle {patente} loaded successfully.")

            print("")
            print(f"{n} VEHICULOS CARGADOS.")

    except FileNotFoundError:
        print(f"File {file.readlines().len()} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

def recaudacionXtorre(garage, torre, anio, mes):
    total = 0
    j = 0   #posición en estacionamiento
    while j < tamanioGar(garage):          #voy recorriendo todo el est
		#print(j)
        a = devolverAuto(garage, j)
        egreso = getHoraEgreso(a)
        if (getTorre(a) == torre and egreso.year == anio and egreso.month == mes):
            total = total + getMonto(a)
        j = j +1
    return total

def reencolar(cola, copia):
    while not colaVacia(copia):
        a = desencolar(copia)
        encolar(cola, a)
    return

def desencolarPorPatente(cola, patente):
    copia = crearCola()
    while not colaVacia(cola):
        a = desencolar(cola)
        if getPatente(a) == patente:
            # viola el tad?
            print(f"Auto {getPatente(a)} eliminado.")
        else:
            encolar(copia, a)
    reencolar(cola, copia)

def cambiarHoraEnCola(cola, patente, horaIngreso):
    copia = crearCola()
    while not colaVacia(cola):
        a = desencolar(cola)
        if getPatente(a) == patente:
            # viola el tad?
            setHoraIngreso(a, horaIngreso)
        encolar(copia, a)
    reencolar(cola, copia)

def printCola(cola):
    copia = crearCola()
    while not colaVacia(cola):
        a = desencolar(cola)
        print("--------------------------------------")
        print("patente: " + getPatente(a))
        cad = getHoraIngreso(a)
        print("Ingreso fecha: " + str(cad.day)+"-"+str(cad.month)+"-"+str(cad.year))
        print("hora ingreso: " + str(cad.hour)+":"+str(cad.minute))
        torre = str(getTorre(a))
        print("torre: " + torre)
        encolar(copia, a)
    reencolar(cola, copia)