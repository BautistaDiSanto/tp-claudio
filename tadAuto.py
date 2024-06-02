def createCar():
	#crea un auto vacío
   # print("Creando auto")		// No se hacen print en los TAD
    auto = ["", None, None, None, None]
    return auto

def fillCar(auto, patente, horaIngreso, horaEgreso, monto, torre):
   # carga los datos del auto
    auto[0] = patente
    auto[1] = horaIngreso
    auto[2] = horaEgreso
    auto[3] = monto
    auto[4] = torre
    

def getPatente(auto):
    return auto[0]

def getHoraIngreso(auto):
    return auto[1]

def getHoraEgreso(auto):
    return auto[2]

def getMonto(auto):
    return auto[3]

def getTorre(auto):
    return auto[4]

def setPatente(auto, patente):
    auto[0] = patente

def setHoraIngreso(auto, horaIngreso):
    auto[1] = horaIngreso

def setHoraEgreso(auto, horaEgreso):
    auto[2] = horaEgreso

def setMonto(auto, monto):
    auto[3] = monto

def setTorre(auto, torre):
    auto[4] = torre
