from models.Evento import Evento  # Importa la clase Evento si ya ha sido convertida a Python

class Filantropico(Evento):
    def __init__(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo, pago_artistas):
        super().__init__(nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo)
        self.patrocinadores = {}  # Un diccionario vacío para almacenar los patrocinadores y sus valores
        self.pago_artistas = pago_artistas


    def asignar_artista(self, nombreArtista, artista):
        self.artistas[nombreArtista] = artista
    def get_hora_inicio(self):
        return self.horaInicio
    def get_direccion(self):
        return self.direccion
    def get_hora_show(self):
        return self.hora_show

    def get_ciudad(self):
        return self.ciudad
    def get_aforo(self):
        return self.aforo
    def get_estado(self):
        return self.estado
    def get_nombre(self):
        return self.nombre

    def get_fecha(self):
        return self.fecha

    def get_lugar(self):
        return self.lugar

    def get_personas(self):
        return self.personas

    def get_precio_preventa(self):
        return self.precioPreventa

    def get_precio_regular(self):
        return self.precioNormal

    def set_precios(self, precioPreventa, precioRegular):
        self.precioPreventa = precioPreventa
        self.precioNormal = precioRegular

    def set_fase_ventas(self, nuevaFase):
        self.fase = nuevaFase

    def set_aforo(self, aforo):
        self.aforo = aforo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora_inicio(self, horaInicio):
        self.horaInicio = horaInicio

    def set_hora_show(self, horaShow):
        self.horaShow = horaShow

    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_estado(self, estado):
        self.estado = estado

    def get_cantidad_asistentes(self):
        return len(self.asistentes)

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
        patrocinadores = ', '.join(self.patrocinadores)
        return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nHora de inicio: {self.hora_inicio}\nHora del show: {self.hora_show}\nLugar: {self.lugar}\nDirección: {self.direccion}\nCiudad: {self.ciudad}\nEstado: {self.estado}\nAforo: {self.aforo}\nPatrocinadores: {patrocinadores}"
    def get_asistentes(self):
        return self.asistentes
    def agregar_boleteria(self, nuevaBoleteria):
        self.boleteria.append(nuevaBoleteria)
    def get_boleteria(self):
        return self.boleteria

    def get_pago_artistas(self):
        # return the payment for the artists for a bar event
        return self.pago_artistas

    def get_pago_alquiler(self):
        return 0
    def asignar_patrocinador(self, patrocinador, valor):
        self.patrocinadores[patrocinador] = valor
    def get_patrocinadores(self):
        return self.patrocinadores