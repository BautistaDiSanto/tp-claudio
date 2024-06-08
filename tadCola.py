def  crearCola():
    return []

def  encolar(cola, elemento):
    cola.append(elemento)

def  desencolar(cola):
    e = cola.pop()
    return e

def  colaVacia(cola):
    return len(cola) == 0

def  tamanioCola(cola):
    return len(cola)

def copiarCola(cola, copia):
    aux = crearCola()
    while not colaVacia(cola):
        a = desencolar(cola)
        encolar(aux, a)
    while not colaVacia(aux):
        a = desencolar(aux)
        encolar(copia, a)
        encolar(cola, a)
