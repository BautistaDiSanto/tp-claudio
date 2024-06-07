from tadAuto import *
from tadGarage import *
from helper import *
import time
import datetime

valorHora = int(input("Ingrese el valor de la hora: "))
autosPico = [0]
estacionamiento = crearEst()
registro = crearEst()
saldoXtorre = [0, 0, 0]

load_vehicles_from_file("cargaAutos.txt", estacionamiento, registro, valorHora, autosPico)

#menu
opcion = None
print("")
print("Creando torres...")
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
    print("9) Eliminar vehiculos a partir de 18hs en torre determinada.")
    print("10) Generar cola por torre.")
    print("0) Salir.")
    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        print("")
        print("INGRESAR VEHICULO")
        patente=input("Ingrese la patente: ")
        ingreso=datetime.datetime.now()
        updateAutosPico(ingreso, autosPico)
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

                updateAutosPico(getHoraIngreso(a), autosPico)

            elif opcionMod == 2:
                new_torre = int(input("Ingrese torre: "))
                setTorre(a, new_torre)

            elif opcionMod == 0:
                print(f"Modificaciones: patente: {getPatente(a)}, torre: {getTorre(a)}, hora ingreso: {getHoraIngreso(a)}")
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
        
        elif opcionElim == "n" or opcionElim == "N":
            print("No se elimino el vehiculo.")	# acá igual esto o aquello => tal cosa
        
        else:
            print("La letra ingresada no es correcta")

    elif opcion == 4:
        print("REGISTRO DE SALIDA DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        i = buscarAuto(estacionamiento, patente)
        a = devolverAuto(estacionamiento, i) 
        
        #setea la hora de salida
        egreso = datetime.datetime.now()
        setHoraEgreso(a, egreso)
        ingreso = getHoraIngreso(a)
        cant_horas = deltaHoras(ingreso, egreso)
        #print(cant_horas)
        
        opcionSalida = input("Desea registrar salida? s/n: ")
        if opcionSalida == "s" or opcionSalida == "S":
            descuento = 1
            #si pertenece a la torre 3 descontar 15% ( x 0,85)
            if getTorre(a) == 3:
                descuento = 0.85
            monto = (cant_horas * valorHora) * descuento  #si descuento == 1, es como si no estuviera
            setMonto(a, round(monto, 2))
            ingresarAuto(registro, a)
            eliminarAuto(estacionamiento, a)
            
            print("el monto de estadía es $" + str(getMonto(a)))
            torre = getTorre(a)
            saldoXtorre[torre-1] = saldoXtorre[torre-1] + getMonto(a)
            
            print("Se registro la salida del vehiculo.")
            
        elif opcionSalida == "n" or opcionSalida == "N":
            print("No se registro la salida del vehiculo.")

        else:
            print("La letra ingresada no es correcta")

    elif opcion == 5:
        print("LISTA DE VEHICULOS EN ESTACIONAMIENTO")
        i = 0

        for i in range(tamanioGar(estacionamiento)):
            print("--------------------------------------")
            a = devolverAuto(estacionamiento, i)
            print("patente: " + getPatente(a))
            cad = getHoraIngreso(a)
            print("Ingreso fecha: " + str(cad.day)+"-"+str(cad.month)+"-"+str(cad.year))
            print("hora ingreso: " + str(cad.hour)+":"+str(cad.minute))
            torre = str(getTorre(a))
            print("torre: " + torre)
        print("FIN DE LA LISTA")
        
    elif opcion == 6:
        print("REGISTRO DE VEHICULOS EGRESADOS")
        for i in range(tamanioGar(registro)):
            print("--------------------------------------")
            a = devolverAuto(registro, i)
            print("patente: " + getPatente(a))
            cad = getHoraIngreso(a)
            print("Ingreso fecha: " + str(cad.day)+"-"+str(cad.month)+"-"+str(cad.year))
            print("hora ingreso: " + str(cad.hour)+":"+str(cad.minute))
            cad = getHoraEgreso(a)
            print("Ingreso fecha: " + str(cad.day)+"-"+str(cad.month)+"-"+str(cad.year))
            print("hora ingreso: " + str(cad.hour)+":"+str(cad.minute))
            monto = getMonto(a)
            print("monto abonado: " + str(monto))
            torre = str(getTorre(a))
            print("torre: " + torre)

    elif opcion == 7:
        print("INFORME DE RECAUDACION POR TORRE")
        torre = int(input("Ingrese numero de torre: "))
        anio = int(input("Ingrese el año del período a considerar: "))
        mes = int(input("Ingrese el mes del período a considerar (número): "))
        total = recaudacionXtorre(registro, torre, anio, mes)
        #a partir de un período determinado (If fecha es mayor que y menor)
        #calcularTorre(t)
        print("el monto recaudado es: " + str(total))

    elif opcion == 8:
        print("")
        print("CANTIDAD DE VEHICULOS EN HORAS PICO")
        print(f"Ingresaron {autosPico[0]} vehiculos entre las 7:00 - 10:00hs y 17:00 - 20:00hs")

    elif opcion == 9:
        print("")
        print("ELIMINAR VEHICULOS A PARTIR DE 18hs EN TORRE DETERMINADA")
        torre = int(input("Ingrese numero de torre: "))
        indices_to_remove = []
        
        for i in range(tamanioGar(estacionamiento)):
            a = devolverAuto(estacionamiento, i)

            if getHoraIngreso(a).hour >= 18 and getTorre(a) == torre:
                indices_to_remove.append(i)

        for index in sorted(indices_to_remove, reverse=True):
            a = devolverAuto(estacionamiento, index)
            eliminarAuto(estacionamiento, a)
            print(f"Se eliminó el vehículo {getPatente(a)}")

    elif opcion == 10:
        print("GENERAR COLA POR TORRE")
        t = input("Ingrese numero de torre: ")
        #colaTorre = generarCola(listaEst,t)
        #print(colaTorre)