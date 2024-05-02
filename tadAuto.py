def crearAuto(patente, horaIngreso, horaEgreso, torre):
    auto = [patente, horaIngreso, horaEgreso, torre]
    return auto

def getPatente(auto):
    return auto[0]

def getHoraIngreso(auto):
    return auto[1]

def getHoraEgreso(auto):
    return auto[2]

def getTorre(auto):
    return auto[3]

def setPatente(auto, patente):
    auto[0] = patente

def setHoraIngreso(auto, horaIngreso):
    auto[1] = horaIngreso

def setHoraEgreso(auto, horaEgreso):
    auto[2] = horaEgreso

def setTorre(auto, torre):
    auto[3] = torre


