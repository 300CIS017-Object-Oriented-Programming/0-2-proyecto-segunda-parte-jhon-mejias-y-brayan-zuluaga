from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nombre, fecha, horaInicio, horaShow, lugar, direccion, ciudad, estado, aforo):
        self.nombre = nombre
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaShow = horaShow
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
    def getNombre(self):
        pass

    @abstractmethod
    def getFecha(self):
        pass

    @abstractmethod
    def getLugar(self):
        pass

    @abstractmethod
    def getPersonas(self):
        pass

    @abstractmethod
    def getCantidadAsistentes(self):
        pass

    @abstractmethod
    def getPrecioPreventa(self):
        pass

    @abstractmethod
    def getPrecioRegular(self):
        pass

    @abstractmethod
    def sumarPersonas(self):
        pass

    @abstractmethod
    def getBoleterias(self):
        pass

    @abstractmethod
    def getAsistentes(self):
        pass

    @abstractmethod
    def getArtistas(self):
        pass

    @abstractmethod
    def getAforo(self):
        pass

    @abstractmethod
    def agregarAsistente(self, asistente):
        pass

    @abstractmethod
    def agregarBoleteria(self, nuevaBoleteria):
        pass
