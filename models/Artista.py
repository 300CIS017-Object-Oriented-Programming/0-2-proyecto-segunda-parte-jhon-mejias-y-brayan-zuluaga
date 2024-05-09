class Artista:
    def __init__(self, nombre, tipoArtista):
        self.nombre = nombre
        self.tipoArtista = tipoArtista
        self.nombreEventos = []

    def getNombre(self):
        return self.nombre

    def agregarNombreEvento(self, nombreEvento):
        self.nombreEventos.append(nombreEvento)

    def getNombreEventos(self):
        return self.nombreEventos
