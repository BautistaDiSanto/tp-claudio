from tadGarage import *
import datetime

#listaEst = crearEst() // crea lista de autos para agregar ingresos
#regisEst = crearEst() // crea registro de autos para cargar luego los que egresan

autosPico = 0

#menu
opcion = None
print("Bienvenido! Ingrese la opcion a realizar: ")
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
    opcion = int(input())
    if opcion == 1:
        print("INGRESAR VEHICULO")
        patente=input("Ingrese la patente: ")
        ingreso=datetime.datetime.now()
        if (int(ingreso.hour) >= 7 and int(ingreso.hour) <= 10) or (int(ingreso.hour) >= 17 and int(ingreso.hour) <= 20):
            autosPico += 1
        #para modificar hora se usa: i = i.replace(hour=int(input()))
        egreso=0
        torre=int(input("Ingrese el numero de torre: "))
        #ingresarAuto(listaEst,patente,ingreso,egreso,torre) //agrega auto a la lista
        print("\nSe agrego el vehiculo...")
        print("PATENTE: ",patente)
        print("HORA DE INGRESO: ",str(ingreso.strftime("%H:%M:%S")))
        print("TORRE NUMERO: ",torre)

    elif opcion == 2:
        print("MODIFICACION DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        i = 0 #invento un indice para probar
        #i = buscarAuto(patente) //busca patente el lista y devuelve indice de ubicacion 
        #si no lo encuentra devuelve None e imprime que el auto no existe en el estacionamiento
        #imprimirAuto(i)
        while i != None:
            print("Ingrese la opcion a realizar: ")
            print("1) Modificar hora de ingreso.")
            print("2) Modificar torre donde se estaciona.")
            print("0) Volver.")
            opcionMod = int(input())
            if opcionMod == 1:
                print("Modifico la hora de ingreso")
                #usar funcion replace para modificar hora y minutos por separado 
                #input("Ingrese hora nueva: ")
                #modificarHoraIngreso(i)
            elif opcionMod == 2:
                print("Modifico torre donde se estaciona.")
                #modificarTorre(i)
            elif opcionMod == 0:
                continue
            else:
                print("El numero ingresado es incorrecto.")
    
    elif opcion == 3:
        print("ELIMINACION DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        i = 0 #invento un indice para probar
        #i = buscarAuto(patente) //busca patente el lista y devuelve indice de ubicacion 
        #imprimirAuto(i)
        opcionElim = input("Desea eliminar este vehiculo? s/n: ")

        if opcionElim == "s":
            #eliminarAuto(i)
            print("Se elimino el vehiculo.")
        elif opcionElim == "S":
            #eliminarAuto(i)
            print("Se elimino el vehiculo.")
        elif opcionElim == "n":
            print("No se elimino el vehiculo.")
        elif opcionElim == "N":
            print("No se elimino el vehiculo.")
        else:
            print("La letra ingresada no es correcta")

    elif opcion == 4:
        print("REGISTRO DE SALIDA DE VEHICULO")
        patente = input("Ingrese patente sin espacios: ")
        i = 0 #invento un indice para probar
        #i = buscarAuto(patente) //busca patente el lista y devuelve indice de ubicacion 
        #imprimirAuto(i)
        opcionSalida = input("Desea registrar salida? s/n: ")
        if opcionSalida == "s":
            #registrarAuto(i)
            print("Se registro la salida del vehiculo.")
        elif opcionSalida == "S":
            #registrarAuto(i)
            print("Se registro la salida del vehiculo.")
        elif opcionSalida == "n":
            print("No se registro la salida del vehiculo.")
        elif opcionSalida == "N":
            print("No se registro la salida del vehiculo.")
        else:
            print("La letra ingresada no es correcta")

    elif opcion == 5:
        print("LISTA DE VEHICULOS EN ESTACIONAMIENTO")
        #imprimirLista(t)?
        """ for x in range(len(listaEst)):
            print (*listaEst, sep="\n")"""
    
    elif opcion == 6:
        print("REGISTRO DE VEHICULOS EGRESADOS")
        #imprimirLista(t)?
    
    elif opcion == 7:
        print("INFORME DE RECAUDACION POR TORRE")
        torre = int(input("Ingrese numero de torre: "))
        #calcularTorre(t)

    elif opcion == 8:
        print("CANTIDAD DE VEHICULOS EN HORAS PICO")
        print("Entre las 7:00 hasta las 10:00hrs y 17:00 hasta las 20:00hrs ingresaron un total de:")
        print(autosPico)

    elif opcion == 9:
        print("ELIMINAR VEHICULOS A PARTIR DE HORA DETERMINADA")
        elimHora = input("Ingrese hora: ")
        #eliminaHora(elimHora)

    elif opcion == 10:
        print("GENERAR COLA POR TORRE")
        t = input("Ingrese numero de torre: ")
        #colaTorre = generarCola(listaEst,t)
        #print(colaTorre)

    """
    FALTA AGREGAR VARIABLE DE LISTAS A LAS FUNCIONES
    """