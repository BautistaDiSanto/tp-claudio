from tadGarage import *
from tadAuto import *
import datetime


def buscarAuto(estacionamiento, patente):
	j = 0   #posición en estacionamiento
	while j < tamanioGar(estacionamiento):          #voy recorriendo todo el est
		a = devolverAuto(estacionamiento, j)
		#si es True tengo que quedarme con ese auto y cortar el bucle
		if (getPatente(a) == patente):
			return j
			break

def load_vehicles_from_file(filename, estacionamiento, valorHora):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
                # Split the line by comma
                data = line.strip().split(', ')
                if len(data) != 4:
                    print(f"Invalid line format: {line}")
                    continue
                
                # Parse the data
                patente = data[0].strip()
                horaIngreso = datetime.datetime.strptime(data[1].strip(), '%H:%M')
                horaEgreso = None

                if data[2].strip() == "null":
                    horaEgreso = None
                else:
                    horaEgreso = datetime.datetime.strptime(data[2].strip(), '%H:%M')
                
                torre = int(data[3].strip())

                # Create and fill the car object
                auto = createCar()
                fillCar(auto, patente, horaIngreso, horaEgreso, None, torre)

                # Add the car to the parking lot
                ingresarAuto(estacionamiento, auto)
                print(f"Vehicle {patente} loaded successfully.")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
