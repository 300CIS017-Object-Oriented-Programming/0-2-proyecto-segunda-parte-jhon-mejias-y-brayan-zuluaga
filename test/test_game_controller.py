import unittest
from unittest.mock import patch
from controllers.game_controller import AdministrarEventos

class TestAdministrarEventos(unittest.TestCase):
    def setUp(self):
        self.administrar_eventos = AdministrarEventos()

    def test_crear_bar(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.assertEqual(len(self.administrar_eventos.bares), 1)
        self.assertEqual(self.administrar_eventos.bares[0].nombre, "Test Bar")

    def test_crear_teatro(self):
        self.administrar_eventos.crear_teatro("Test Theater", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.assertEqual(len(self.administrar_eventos.teatros), 1)
        self.assertEqual(self.administrar_eventos.teatros[0].nombre, "Test Theater")

    def test_crear_filantropico(self):
        self.administrar_eventos.crear_filantropico("Test Philanthropic", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, "Test Sponsor")
        self.assertEqual(len(self.administrar_eventos.filantropicos), 1)
        self.assertEqual(self.administrar_eventos.filantropicos[0].nombre, "Test Philanthropic")

    def test_eliminar_evento(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.assertEqual(len(self.administrar_eventos.bares), 1)
        self.administrar_eventos.eliminar_evento("bar", "Test Bar")
        self.assertEqual(len(self.administrar_eventos.bares), 0)

    def test_vender_boletas(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.administrar_eventos.vender_boletas("bar", "Test Bar", "Test Name", "Test Lastname", 30, "Test Street", "Test Medium", "preventa", "efectivo", 10)
        self.assertEqual(self.administrar_eventos.bares[0].asistentes[0].nombre, "Test Name")

    def test_buscar_evento(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        evento = self.administrar_eventos.buscar_evento("bar", "Test Bar")
        self.assertEqual(evento.nombre, "Test Bar")

    def test_registrar_ingreso(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.administrar_eventos.vender_boletas("bar", "Test Bar", "Test Name", "Test Lastname", 30, "Test Street", "Test Medium", "preventa", "efectivo", 10)
        self.administrar_eventos.registrar_ingreso("Test Name", "bar")
        self.assertEqual(self.administrar_eventos.bares[0].asistentes[0].boletas, 9)

if __name__ == '__main__':
    unittest.main()