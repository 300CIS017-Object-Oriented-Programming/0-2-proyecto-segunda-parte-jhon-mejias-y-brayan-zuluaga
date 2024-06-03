class Asistente:
    def __init__(self, nombre, apellido, edad, direccion, medio_enterado):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.medio_enterado = medio_enterado
        self.boletas = 0
        self.confirmacion = False

    def get_nombre(self):
        return self.nombre

    def get_boletas(self):
        return self.boletas

    def comprar_boleta(self):
        self.boletas += 1

    def usarBoleta(self):
        if self.boletas > 0:
            self.boletas -= 1
    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_direccion(self):
        return self.direccion

    def get_medio_enterado(self):
        return self.medio_enterado
    def get_confirmacion(self):
        return self.confirmacion
    def get_boletas_compradas(self):
        return self.boletas