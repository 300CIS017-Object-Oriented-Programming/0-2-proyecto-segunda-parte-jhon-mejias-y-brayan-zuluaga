class Artista:
    def __init__(self, nombre, tipo_artista):
        self.nombre = nombre
        self.tipoArtista = tipo_artista
        self.nombre_eventos = []

    def getNombre(self):
        return self.nombre

    def getNombreEventos(self):
        return self.nombre_eventos
    def agregar_nombre_evento(self, nombre_evento):
        self.nombre_eventos.append(nombre_evento)