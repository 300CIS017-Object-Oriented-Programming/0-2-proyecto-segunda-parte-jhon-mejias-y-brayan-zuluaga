class Boleteria:
    def __init__(self, tipoBoleteria, precioPreventa, precioRegular, metodoPago):
        self.tipoBoleteria = tipoBoleteria
        self.precioPreventa = precioPreventa
        self.precioRegular = precioRegular
        self.metodoPago = metodoPago
        self.utilidad = 0.0  # Por defecto la utilidad es 0.0

    def getTipoBoleteria(self):
        return self.tipoBoleteria

    def getPrecioPreventa(self):
        return self.precioPreventa

    def getPrecioRegular(self):
        return self.precioRegular

    def getMetodoPago(self):
        return self.metodoPago

    def setPrecios(self, precioPreventa, precioRegular):
        self.precioPreventa = precioPreventa
        self.precioRegular = precioRegular
