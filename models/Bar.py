from models.Evento import Evento


class Bar(Evento):
    def __init__(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo,pago_artistas, maximo_preventa, maximo_cortesia):
        super().__init__(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)
        self.pago_artistas = pago_artistas
        self.maximo_preventa = maximo_preventa
        self.maximo_cortesia = maximo_cortesia
    def pagar_comediante(self):
        # Implementa la lógica para pagar al comediante si es necesario
        pass

    def asignar_artista(self, nombre_artista, artista):
        self.artistas[nombre_artista] = artista

    def get_nombre(self):
        return self.nombre

    def get_fecha(self):
        return self.fecha
    def get_aforo(self):
        return self.aforo
    def get_lugar(self):
        return self.lugar
    def get_hora_inicio(self):
        return self.hora_inicio
    def get_hora_show(self):
        return self.hora_show
    def get_ciudad(self):
        return self.ciudad
    def get_estado(self):
        return self.estado
    def get_direccion(self):
        return self.direccion
    def get_personas(self):
        return self.personas

    def get_precio_preventa(self):
        return self.precio_preventa

    def get_precio_regular(self):
        return self.precio_normal

    def set_precios(self, precio_preventa, precio_regular):
        self.precio_preventa = precio_preventa
        self.precio_normal = precio_regular

    def set_fase_ventas(self, nueva_fase):
        self.fase = nueva_fase

    def set_aforo(self, aforo):
        self.aforo = aforo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def set_hora_show(self, hora_show):
        self.hora_show = hora_show

    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_estado(self, estado):
        self.estado = estado

    def get_cantidad_asistentes(self):
        return self.personas

    def sumar_personas(self):
        self.personas += 1

    def get_boleterias(self):
        return self.boleteria

    def get_aforo(self):
        return self.aforo

    def agregar_asistente(self, asistente):
        self.asistentes.append(asistente)

    def get_asistente(self):
        return self.asistentes

    def get_artistas(self):
        return self.artistas

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nHora de inicio: {self.hora_inicio}\nHora del show: {self.hora_show}\nLugar: {self.lugar}\nDirección: {self.direccion}\nCiudad: {self.ciudad}\nEstado: {self.estado}\nAforo: {self.aforo}\nPago a artistas: {self.pago_artistas}"


    def get_asistentes(self):
        return self.asistentes

    def agregar_boleteria(self, nueva_boleteria):
        self.boleteria.append(nueva_boleteria)
    def get_boleteria(self):
        return self.boleteria
    def get_pago_artistas(self):
        # return the payment for the artists for a bar event
        return self.pago_artistas

    def get_pago_alquiler(self):
        return 0
    
    def get_patrocinadores(self):
        return []

    def get_maximo_preventa(self):
        return self.maximo_preventa
    def get_maximo_cortesia(self):
        return self.maximo_cortesia
    def set_maximo_preventa(self, maximo_preventa):
        self.maximo_preventa = maximo_preventa
    def set_maximo_cortesia(self, maximo_cortesia):
        self.maximo_cortesia = maximo_cortesia