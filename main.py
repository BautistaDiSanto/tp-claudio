from tadAuto import *
from tadGarage import *
from helper import *
import datetime

autosPico = 0

valorHora = int(input("Ingrese el valor de la hora: "))
estacionamiento = crearEst()

load_vehicles_from_file("cargaAutos.txt", estacionamiento, valorHora)

#menu
opcion = None
print("")
print("Creando torres...")
registro = crearEst()
print("")
print("Bienvenido!")

while opcion != 0:
    print("\n1) Ingresar vehiculo.")
    print("2) Modificar vehiculo.")
    print("3) Eliminar vehiculo.")
    print("4) Registrar salida vehiculo.")
    print("5) Lista de vehiculos en estacionamiento.")
    print("6) Registro de vehiculos egresados.")
    print("7) Informe de reacaudacion por torre.")
    print("8) Cantidad de vehiculos en horas pico.")
    print("9) Eliminar vehiculos a partir de hora determinada.")
    print("10) Generar cola por torre.")
    print("0) Salir.")
    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        print("")
        print("INGRESAR VEHICULO")
        patente=input("Ingrese la patente: ")
        ingreso=datetime.datetime.now()

        if (int(ingreso.hour) >= 7 and int(ingreso.hour) <= 10) or (int(ingreso.hour) >= 17 and int(ingreso.hour) <= 20):
            autosPico += 1

        torre=int(input("Ingrese el numero de torre: "))
        auto = createCar()
        fillCar(auto, patente, ingreso, None, None, torre)
        ingresarAuto(estacionamiento, auto)

    elif opcion == 2:
        print("")
        print("MODIFICACION DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        j = 0	#posición en estacionamiento

        while j < tamanioGar(estacionamiento):
            a = devolverAuto(estacionamiento, j)

            if (getPatente(a) == patente):
                break 	#???

            j += 1
		
        a = devolverAuto(estacionamiento, j)

        while j != None:
            print("")
            print("1) Modificar hora de ingreso.")
            print("2) Modificar torre donde se estaciona.")
            print("0) Volver.")
            opcionMod = int(input("Ingrese la opcion a realizar: "))

            if opcionMod == 1:
                print("")
                current_time = getHoraIngreso(a)
                updated_time = current_time.replace(hour=int(input("Ingrese nueva hora (0-23): ")), minute=int(input("Ingrese nuevos minutos (0-59): ")))
                setHoraIngreso(a, updated_time)

                if (int(getHoraIngreso(a).hour) >= 7 and int(getHoraIngreso(a).hour) <= 10) or (int(getHoraIngreso(a).hour) >= 17 and int(getHoraIngreso(a).hour) <= 20):
                    autosPico += 1

            elif opcionMod == 2:
                new_torre = int(input("Ingrese torre: "))
                setTorre(a, new_torre)

            elif opcionMod == 0:
                print(f"Modificaciones: {a}")
                break

            else:
                print("El numero ingresado es incorrecto.")
    
    elif opcion == 3:
        print("ELIMINACION DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        j = buscarAuto(estacionamiento, patente)
        opcionElim = input("Desea eliminar este vehiculo? s/n: ")

        if opcionElim == "s" or opcionElim == "S":
            a = devolverAuto(estacionamiento, j)
            eliminarAuto(estacionamiento, a)		#i es el auto filtrado
            print("Se elimino el vehiculo.")
        #elif opcionElim == "S":			#esto habría que ponerlo como 'o' con el anterior
            #eliminarAuto(i)
        #    print("Se elimino el vehiculo.")
        elif opcionElim == "n" or opcionElim == "N":
            print("No se elimino el vehiculo.")	# acá igual esto o aquello => tal cosa
        #elif opcionElim == "N":
        #    print("No se elimino el vehiculo.")
        else:
            print("La letra ingresada no es correcta")

    elif opcion == 4:
        print("REGISTRO DE SALIDA DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        i = buscarAuto(estacionamiento, patente)
        a = devolverAuto(estacionamiento, i) 
        #imprimirAuto(i)
        opcionSalida = input("Desea registrar salida? s/n: ")
        if opcionSalida == "s" or opcionSalida == "S":
            #AGREGAR COBRO (Si torre es 3 aplicar descuento)
            registrarAuto(registro, a)
            eliminarAuto(estacionamiento, a)
            
            print("Se registro la salida del vehiculo.")
        #elif opcionSalida == "S":
            #registrarAuto(i)
        #    print("Se registro la salida del vehiculo.")
        elif opcionSalida == "n" or opcionSalida == "N":
            print("No se registro la salida del vehiculo.")
        #elif opcionSalida == "N":
        #    print("No se registro la salida del vehiculo.")
        else:
            print("La letra ingresada no es correcta")

    elif opcion == 5:
        print("LISTA DE VEHICULOS EN ESTACIONAMIENTO")
        i = 0

        for i in range(tamanioGar(estacionamiento)):
            a = devolverAuto(estacionamiento, i)
            print(a)            
    
    elif opcion == 6:
        print("REGISTRO DE VEHICULOS EGRESADOS")
        #imprimirLista(t)?
        for i in range(tamanioGar(registro)):
            a = devolverAuto(registro, i)
            print("patente: " + getPatente(a))
            cad = str(getHoraIngreso(a))
            print("hora ingreso: " + cad)
            #hora egreso
            #monto
            torre = str(getTorre(a))
            print("torre: " + torre)
    elif opcion == 7:
        print("INFORME DE RECAUDACION POR TORRE")
        torre = int(input("Ingrese numero de torre: "))
        #calcularTorre(t)

    elif opcion == 8:
        print("")
        print("CANTIDAD DE VEHICULOS EN HORAS PICO")
        print(f"Ingresaron {autosPico} vehiculos entre las 7:00 - 10:00hs y 17:00 - 20:00hs")

    elif opcion == 9:
        print("ELIMINAR VEHICULOS A PARTIR DE HORA DETERMINADA")
        elimHora = input("Ingrese hora: ")
        #eliminaHora(elimHora)

    elif opcion == 10:
        print("GENERAR COLA POR TORRE")
        t = input("Ingrese numero de torre: ")
        #colaTorre = generarCola(listaEst,t)
        #print(colaTorre)

