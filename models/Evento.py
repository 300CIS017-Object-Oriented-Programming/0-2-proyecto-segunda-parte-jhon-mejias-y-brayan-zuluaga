from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nombre, fecha, hora_inicio, hora_show, lugar, direccion, ciudad, estado, aforo):
        self.nombre = nombre
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_show = hora_show
        self.lugar = lugar
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.fase = ""  # En C++ no se utiliza este atributo, por lo que puedes eliminarlo o asignarle un valor por defecto
        self.personas = 0  # Por defecto no hay personas en el evento
        self.precioPreventa = 0  # Por defecto no hay precio de preventa
        self.precioNormal = 0  # Por defecto no hay precio normal
        self.aforo = aforo
        self.utilidad = 0.0  # Por defecto la utilidad es 0.0
        self.artistas = {}  # Un diccionario vacío para almacenar los artistas
        self.asistentes = []  # Una lista vacía para almacenar los asistentes
        self.boleteria = []  # Una lista vacía para almacenar la boletería

    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_fecha(self):
        pass

    @abstractmethod
    def get_lugar(self):
        pass

    @abstractmethod
    def get_personas(self):
        pass

    @abstractmethod
    def get_cantidad_asistentes(self):
        pass

    @abstractmethod
    def get_precio_preventa(self):
        pass

    @abstractmethod
    def get_precio_regular(self):
        pass

    @abstractmethod
    def sumar_personas(self):
        pass

    @abstractmethod
    def get_boleterias(self):
        pass

    @abstractmethod
    def get_asistentes(self):
        pass

    @abstractmethod
    def get_artistas(self):
        pass

    @abstractmethod
    def get_aforo(self):
        pass

    @abstractmethod
    def agregar_asistente(self, asistente):
        pass

    @abstractmethod
    def agregar_boleteria(self, nuevaBoleteria):
        pass

    @abstractmethod
    def get_boleteria(self):
        pass