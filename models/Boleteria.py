class Boleteria:
    def __init__(self, tipo_boleteria, precio_preventa, precio_regular, metodo_pago):
        self.tipo_boleteria = tipo_boleteria
        self.precio_preventa = precio_preventa
        self.precio_regular = precio_regular
        self.metodo_pago = metodo_pago
        self.utilidad = 0.0  # Por defecto la utilidad es 0.0

    def get_tipo_boleteria(self):
        return self.tipo_boleteria

    def get_precio_preventa(self):
        return self.precio_preventa

    def get_precio_regular(self):
        return self.precio_regular

    def get_metodo_pago(self):
        return self.metodo_pago

    def set_precios(self, precio_preventa, precio_regular):
        self.precio_preventa = precio_preventa
        self.precio_regular = precio_regular