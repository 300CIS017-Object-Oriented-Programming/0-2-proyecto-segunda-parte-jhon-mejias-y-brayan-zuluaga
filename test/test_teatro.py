import unittest
from models.Teatro import Teatro
from controllers.game_controller import AdministrarEventos
from unittest.mock import MagicMock
class TestTeatro(unittest.TestCase):

    def setUp(self):
        self.teatro = Teatro("Test Event", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Address", "Test City", "Open", 100, 1000)

    def test_get_asistentes(self):
        self.assertEqual(self.teatro.get_asistentes(), [])

    def test_get_hora_inicio(self):
        self.assertEqual(self.teatro.get_hora_inicio(), "18:00")

    def test_get_hora_show(self):
        self.assertEqual(self.teatro.get_hora_show(), "20:00")

    def test_get_aforo(self):
        self.assertEqual(self.teatro.get_aforo(), 100)

    def test_get_ciudad(self):
        self.assertEqual(self.teatro.get_ciudad(), "Test City")

    def test_get_estado(self):
        self.assertEqual(self.teatro.get_estado(), "Open")

    def test_costo_alquiler(self):
        self.assertIsNone(self.teatro.costo_alquiler())

    def test_get_costo_alquiler(self):
        self.assertEqual(self.teatro.get_costo_alquiler(), 0)

    def test_asignar_artista(self):
        artist_mock = MagicMock()
        self.teatro.asignar_artista("Test Artist", artist_mock)
        self.assertIn("Test Artist", self.teatro.get_artistas())

    def test_get_nombre(self):
        self.assertEqual(self.teatro.get_nombre(), "Test Event")

    def test_get_direccion(self):
        self.assertEqual(self.teatro.get_direccion(), "Test Address")

    def test_get_fecha(self):
        self.assertEqual(self.teatro.get_fecha(), "2023-12-31")

    def test_get_lugar(self):
        self.assertEqual(self.teatro.get_lugar(), "Test Venue")

    def test_get_personas(self):
        self.assertEqual(self.teatro.get_personas(), 0)




    def test_set_precios(self):
        self.teatro.set_precios(50, 100)
        self.assertEqual(self.teatro.get_precio_preventa(), 50)
        self.assertEqual(self.teatro.get_precio_regular(), 100)

    def test_set_fase_ventas(self):
        self.teatro.set_fase_ventas("Preventa")
        self.assertEqual(self.teatro.fase, "Preventa")

    def test_set_aforo(self):
        self.teatro.set_aforo(200)
        self.assertEqual(self.teatro.get_aforo(), 200)

    def test_set_nombre(self):
        self.teatro.set_nombre("New Event")
        self.assertEqual(self.teatro.get_nombre(), "New Event")

    def test_set_fecha(self):
        self.teatro.set_fecha("2024-01-01")
        self.assertEqual(self.teatro.get_fecha(), "2024-01-01")

    def test_set_hora_inicio(self):
        self.teatro.set_hora_inicio("19:00")
        self.assertEqual(self.teatro.get_hora_inicio(), "19:00")

    def test_set_hora_show(self):
        self.teatro.set_hora_show("21:00")
        self.assertEqual(self.teatro.get_hora_show(), "21:00")

    def test_set_lugar(self):
        self.teatro.set_lugar("New Venue")
        self.assertEqual(self.teatro.get_lugar(), "New Venue")

    def test_set_direccion(self):
        self.teatro.set_direccion("New Address")
        self.assertEqual(self.teatro.get_direccion(), "New Address")

    def test_set_ciudad(self):
        self.teatro.set_ciudad("New City")
        self.assertEqual(self.teatro.get_ciudad(), "New City")

    def test_set_estado(self):
        self.teatro.set_estado("Closed")
        self.assertEqual(self.teatro.get_estado(), "Closed")

    def test_get_cantidad_asistentes(self):
        self.assertEqual(self.teatro.get_cantidad_asistentes(), 0)

    def test_get_boleterias(self):
        self.assertEqual(self.teatro.get_boleterias(), [])

    def test_get_asistente(self):
        self.assertEqual(self.teatro.get_asistente(), [])

    def test_get_aforo(self):
        self.assertEqual(self.teatro.get_aforo(), 100)

    def test_get_artistas(self):
        self.assertEqual(self.teatro.get_artistas(), {})

    def test_agregar_asistente(self):
        asistente_mock = MagicMock()
        self.teatro.agregar_asistente(asistente_mock)
        self.assertEqual(self.teatro.get_cantidad_asistentes(), 1)

    def test_mostrar_detalles(self):
        detalles = self.teatro.mostrar_detalles()
        self.assertIn("Test Event", detalles)
        self.assertIn("Test Venue", detalles)

    def test_sumar_personas(self):
        self.teatro.sumar_personas()
        self.assertEqual(self.teatro.get_personas(), 1)

    def test_agregar_boleteria(self):
        boleteria_mock = MagicMock()
        self.teatro.agregar_boleteria(boleteria_mock)
        self.assertEqual(len(self.teatro.get_boleteria()), 1)

    def test_get_pago_artistas(self):
        self.assertEqual(self.teatro.get_pago_artistas(), 1000)

    def test_get_pago_alquiler(self):
        self.assertEqual(self.teatro.get_pago_alquiler(), 0)

    def test_get_patrocinadores(self):
        self.assertEqual(self.teatro.get_patrocinadores(), [])

if __name__ == '__main__':
    unittest.main()