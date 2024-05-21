class Asistente:
    def __init__(self, nombre, apellido, edad, direccion, medioEnterado):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.medioEnterado = medioEnterado
        self.boletas = 0

    def getNombre(self):
        return self.nombre

    def getBoletas(self):
        return self.boletas

    def comprarBoleta(self):
        self.boletas += 1

    def usarBoleta(self):
        if self.boletas > 0:
            self.boletas -= 1
    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def getDireccion(self):
        return self.direccion

    def getMedioEnterado(self):
        return self.medioEnterado
