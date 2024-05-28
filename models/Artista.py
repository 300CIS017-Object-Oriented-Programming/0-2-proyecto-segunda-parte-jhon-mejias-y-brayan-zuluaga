class Artista:
    def __init__(self, nombre, tipo_artista):
        self.nombre = nombre
        self.tipoArtista = tipo_artista
        self.eventos = {}

    def getNombre(self):
        return self.nombre

    def getNombreEventos(self):
        return self.eventos
    def agregar_evento(self, tipo_evento, nombre_evento):
        if tipo_evento not in self.eventos:
            self.eventos[tipo_evento] = []
        self.eventos[tipo_evento].append(nombre_evento)