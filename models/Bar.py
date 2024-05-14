from models.Evento import Evento


class Bar(Evento):
    def __init__(self, nombre, fecha, horaInicio, horaShow, lugar, direccion, ciudad, estado, aforo,pago_artistas):
        super().__init__(nombre, fecha, horaInicio, horaShow, lugar, direccion, ciudad, estado, aforo)
        self.pago_artistas = pago_artistas
    def pagarComediante(self):
        # Implementa la lógica para pagar al comediante si es necesario
        pass

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

    def sumarPersonas(self):
        self.personas += 1

    def getBoleterias(self):
        return self.boleteria

    def getAforo(self):
        return self.aforo

    def agregarAsistente(self, asistente):
        self.asistentes.append(asistente)

    def getAsistente(self):
        return self.asistentes

    def getArtistas(self):
        return self.artistas

    def mostrarDetalles(self):
        # Implementa la lógica para mostrar los detalles del evento (nombre, fecha, lugar, etc.)
        pass
    def getAsistentes(self):
        pass
    def agregarBoleteria(self, nuevaBoleteria):
        self.boleteria.append(nuevaBoleteria)
