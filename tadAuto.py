def createCar():
	#crea un auto vacío
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

def getTorre(auto):
    return auto[4]

def setPatente(auto, patente):
    auto[0] = patente

def setHoraIngreso(auto, horaIngreso):
    auto[1] = horaIngreso

def setHoraEgreso(auto, horaEgreso):
    auto[2] = horaEgreso

def setTorre(auto, torre):
    auto[4] = torre
