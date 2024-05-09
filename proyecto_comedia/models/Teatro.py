from models.Evento import Evento  # Importa la clase Evento si ya ha sido convertida a Python

class Teatro(Evento):
    def __init__(self, nombre, fecha, horaInicio, horaShow, lugar, direccion, ciudad, estado, aforo):
        super().__init__(nombre, fecha, horaInicio, horaShow, lugar, direccion, ciudad, estado, aforo)
        self.costo = 0

    def costoAlquiler(self):
        # Implementa la lógica para calcular el costo del alquiler del teatro si es necesario
        pass

    def getCostoAlquiler(self):
        return self.costo

    def asignarArtista(self, nombreArtista, artista):
        self.artistas[nombreArtista] = artista

    def getNombre(self):
        return self.nombre

    def getFecha(self):
        return self.fecha

    def getLugar(self):
        return self.lugar

    def getPersonas(self):
        return self.personas

    def getPrecioPreventa(self):
        return self.precioPreventa

    def getPrecioRegular(self):
        return self.precioNormal

    def setPrecios(self, precioPreventa, precioRegular):
        self.precioPreventa = precioPreventa
        self.precioNormal = precioRegular

    def setFaseVentas(self, nuevaFase):
        self.fase = nuevaFase

    def setAforo(self, aforo):
        self.aforo = aforo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFecha(self, fecha):
        self.fecha = fecha

    def setHoraInicio(self, horaInicio):
        self.horaInicio = horaInicio

    def setHoraShow(self, horaShow):
        self.horaShow = horaShow

    def setLugar(self, lugar):
        self.lugar = lugar

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def setEstado(self, estado):
        self.estado = estado

    def getCantidadAsistentes(self):
        return len(self.asistentes)

    def getBoleterias(self):
        return self.boleteria

    def getAsistente(self):
        return self.asistentes

    def getAforo(self):
        return self.aforo

    def getArtistas(self):
        return self.artistas

    def agregarAsistente(self, asistente):
        self.asistentes.append(asistente)

    def mostrarDetalles(self):
        # Implementa la lógica para mostrar los detalles del evento (nombre, fecha, lugar, etc.)
        pass

    def sumarPersonas(self):
        self.personas += 1

    def agregarBoleteria(self, nuevaBoleteria):
        self.boleteria.append(nuevaBoleteria)
