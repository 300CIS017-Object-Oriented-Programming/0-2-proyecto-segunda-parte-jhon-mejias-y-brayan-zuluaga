from typing import List, Dict
class GuiController:
    def __init__(self):
        #self.filantropicos: List[Filantropico] = []
        #self.bares: List[Bar] = []
        #self.teatros: List[Teatro] = []
        #self.artistas: Dict[str, Artista] = {}
        self.menu = True
        self.creando_evento = False
        self.mostrando_eventos = False
        self.editando_evento = False
        self.eliminando_evento = False
        self.generando_reportes = False
        self.vendiendo_boletas = False
        self.creando_artista = False
        self.asignando_artista = False
        self.mostrando_detalles_evento = False
        self.imprimiendo_eventos = False
        self.registrar_ingreso = False
        self.mostrar_reportes = False
        self.asignar_patrocinador = False
        self.dashboard = False
        self.asignar_precios_boletas = False

    def activate_asignar_precios_boletas(self):
        self.asignar_precios_boletas = True
    def activate_dashboard(self):
        self.dashboard = True
    def activate_menu(self):
        self.menu = True
    def activate_creando_evento(self):
        self.creando_evento = True
    def activate_editando_evento(self):
        self.editando_evento = True
    def activate_eliminando_evento(self):
        self.eliminando_evento = True
    def activate_asignar_patrocinador(self):
        self.asignar_patrocinador = True

    def activate_generando_reportes(self):
        self.generando_reportes = True
    def activate_vendiendo_boletas(self):
        self.vendiendo_boletas = True
    def activate_creando_artista(self):
        self.creando_artista = True
    def activate_asignando_artista(self):
        self.asignando_artista = True
    def activate_mostrando_detalles_evento(self):
        self.mostrando_detalles_evento = True
    def activate_imprimiendo_eventos(self):
        self.imprimiendo_eventos = True
    def activate_registrar_ingreso(self):
        self.registrar_ingreso = True
    def activate_mostrar_reportes(self):
        self.mostrar_reportes = True
    def desactivate_dashboard(self):
        self.dashboard = False
    def desactivate_asignar_patrocinador(self):
        self.asignar_patrocinador = False
    def desactivate_registrar_ingreso(self):
        self.registrar_ingreso = False
    def desactivate_mostrar_reportes(self):
        self.mostrar_reportes = False
    def desactivate_asignar_precios_boletas(self):
        self.asignar_precios_boletas = False
    def desactivate_menu(self):
        self.menu = False
    def desactivate_creando_evento(self):
        self.creando_evento = False
    def desactivate_editando_evento(self):
        self.editando_evento = False
    def desactivate_eliminando_evento(self):
        self.eliminando_evento = False
    def desactivate_generando_reportes(self):
        self.generando_reportes = False
    def desactivate_vendiendo_boletas(self):
        self.vendiendo_boletas = False
    def desactivate_creando_artista(self):
        self.creando_artista = False
    def desactivate_asignando_artista(self):
        self.asignando_artista = False
    def desactivate_mostrando_detalles_evento(self):
        self.mostrando_detalles_evento = False
    def desactivate_imprimiendo_eventos(self):
        self.imprimiendo_eventos = False
    def get_asignar_precios_boletas(self):
        return self.asignar_precios_boletas
    def get_dashboard(self):
        return self.dashboard
    def get_menu(self):
        return self.menu
    def get_creando_evento(self):
        return self.creando_evento
    def get_editando_evento(self):
        return self.editando_evento
    def get_eliminando_evento(self):
        return self.eliminando_evento
    def get_generando_reportes(self):
        return self.generando_reportes
    def get_vendiendo_boletas(self):
        return self.vendiendo_boletas
    def get_creando_artista(self):
        return self.creando_artista
    def get_asignando_artista(self):
        return self.asignando_artista
    def get_mostrando_detalles_evento(self):
        return self.mostrando_detalles_evento
    def get_imprimiendo_eventos(self):
        return self.imprimiendo_eventos
    def get_registrar_ingreso(self):
        return self.registrar_ingreso
    def get_mostrar_reportes(self):
        return self.mostrar_reportes
    def get_asignar_patrocinador(self):
        return self.asignar_patrocinador