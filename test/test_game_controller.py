import unittest
from unittest.mock import patch, call
from controllers.game_controller import AdministrarEventos

class TestAdministrarEventos(unittest.TestCase):
    def setUp(self):
        self.administrar_eventos = AdministrarEventos()

    def test_crear_bar(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.assertEqual(len(self.administrar_eventos.bares), 1)
        self.assertEqual(self.administrar_eventos.bares[0].nombre, "Test Bar")

    def test_crear_filantropico(self):
        self.administrar_eventos.crear_filantropico("Test Philanthropic", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, "Test Sponsor")
        self.assertEqual(len(self.administrar_eventos.filantropicos), 1)
        self.assertEqual(self.administrar_eventos.filantropicos[0].nombre, "Test Philanthropic")


    def test_registrar_ingreso_asistente(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.administrar_eventos.vender_boletas("Bar", "Test Bar", "Test Name", "Test Lastname", 30, "Test Street", "Test Medium", "preventa", "efectivo", 10)
        result = self.administrar_eventos.registrar_ingreso("Test Bar", "Bar", "Test Name")
        self.assertTrue(result)

    def test_vender(self):
        self.administrar_eventos.crear_bar("Barr", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        result = self.administrar_eventos.vender_boletas("Bar", "Barr", "Name", "Lastname", 30, "Test Street", "Test Medium", "preventa", "efectivo", 1)
        self.assertTrue(result)

    @patch('reportlab.pdfgen.canvas.Canvas')
    def test_successful_ticket_generation(self, mock_canvas):
        result = self.administrar_eventos.generar_boleta("Test Name", "Test Lastname", 30, "Test Street", "Test Medium", "preventa", 10, 50000, "Test Event", "2023-12-31", "18:00", "Test Venue", "Test Street", "20:00", "Test City", "Test State", 100, "bar")
        self.assertTrue(mock_canvas.called)

    def test_pricing_for_preventa_boleta(self):
        result = self.administrar_eventos.precio_boleta("preventa")
        self.assertEqual(result, 5000)

    def test_pricing_for_regular_boleta(self):
        result = self.administrar_eventos.precio_boleta("regular")
        self.assertEqual(result, 10000)

    def test_pricing_for_cortesia_boleta(self):
        result = self.administrar_eventos.precio_boleta("cortesia")
        self.assertEqual(result, 0)


    @patch('builtins.print')
    def test_imprimir_eventos(self, mock_print):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000)
        self.administrar_eventos.crear_teatro("Test Theater", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 1000,1000)
        self.administrar_eventos.crear_filantropico("Test Philanthropic", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, "Test Sponsor")
        self.administrar_eventos.imprimir_eventos()
        calls = [call("Eventos de tipo Bar:"), call("Test Bar"), call("Eventos de tipo Teatro:"), call("Test Theater"), call("Eventos de tipo Filantropico:"), call("Test Philanthropic")]
        mock_print.assert_has_calls(calls, any_order=False)

    def test_crear_artista_with_new_artist(self):
        result = self.administrar_eventos.crear_artista("New Artist", "Musician")
        self.assertTrue(result)
        self.assertEqual(self.administrar_eventos.artistas["New Artist"].nombre, "New Artist")

    def test_artist_assigned_to_bar_event(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street",
                                           "Test City", "Test State", 100, 1000)
        self.administrar_eventos.crear_artista("Test Artist", "Musician")
        result = self.administrar_eventos.asignar_artista("Bar", "Test Bar", "Test Artist")
        self.assertTrue(result)

    def test_multiple_artists_assigned_to_bar_event(self):
        self.administrar_eventos.crear_bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street",
                                           "Test City", "Test State", 100, 1000)
        self.administrar_eventos.crear_artista("Test Artist 1", "Musician")
        self.administrar_eventos.crear_artista("Test Artist 2", "Musician")
        result1 = self.administrar_eventos.asignar_artista("Bar", "Test Bar", "Test Artist 1")
        result2 = self.administrar_eventos.asignar_artista("Bar", "Test Bar", "Test Artist 2")
        self.assertTrue(result1)
        self.assertTrue(result2)


if __name__ == '__main__':
    unittest.main()