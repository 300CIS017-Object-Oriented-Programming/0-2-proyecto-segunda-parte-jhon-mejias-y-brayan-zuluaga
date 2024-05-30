class Artista:
    def __init__(self, nombre, tipo_artista):
        self.nombre = nombre
        self.tipo_artista = tipo_artista
        self.eventos = {}

    def get_nombre(self):
        return self.nombre

    def get_nombre_eventos(self):
        return self.eventos
    def agregar_evento(self, tipo_evento, nombre_evento):
        if tipo_evento not in self.eventos:
            self.eventos[tipo_evento] = []
        self.eventos[tipo_evento].append(nombre_evento)

    def get_eventos(self):
        return self.eventos