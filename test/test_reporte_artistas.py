import unittest
from models.Artista import Artista
from controllers.game_controller import AdministrarEventos

class TestAdministrarEventos(unittest.TestCase):
    def setUp(self):
        self.administrar_eventos = AdministrarEventos()

    def artist_report_returns_correct_data_when_artist_exists(self):
        # Add an artist
        self.administrar_eventos.crear_artista("Test Artist", "Musician")

        # Add a bar event with the artist
        self.administrar_eventos.crear_bar("Test Event", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Address", "Test City", "Open", 100, 1000)
        self.administrar_eventos.asignar_artista("Bar", "Test Event", "Test Artist")

        # Generate the artist report
        report = self.administrar_eventos.generar_reporte_artistas("Test Artist")

        # Check that the report contains the correct data
        self.assertEqual(report["nombre_evento"].values[0], "Test Event")
        self.assertEqual(report["boletas_vendidas"].values[0], 0)
        self.assertEqual(report["porcentaje_aforo"].values[0], 0)

    def artist_report_returns_none_when_artist_does_not_exist(self):
        # Generate the artist report
        report = self.administrar_eventos.generar_reporte_artistas("Nonexistent Artist")

        # Check that the report is None
        self.assertIsNone(report)

if __name__ == '__main__':
    unittest.main()