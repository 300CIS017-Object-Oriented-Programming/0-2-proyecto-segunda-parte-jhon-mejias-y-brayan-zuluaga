import unittest
from models.Filantropico import Filantropico
from controllers.game_controller import AdministrarEventos

class TestAdministrarEventos(unittest.TestCase):
    def setUp(self):
        self.administrar_eventos = AdministrarEventos()

    def test_patrocinadores_evento_returns_sponsors_when_event_exists(self):
        # Add a philanthropic event with a sponsor
        filantropico = Filantropico("Test Event", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Address", "Test City", "Open", 100, 1000)
        filantropico.asignar_patrocinador("Test Sponsor", 500)
        self.administrar_eventos.filantropicos.append(filantropico)

        # Check that the sponsors are returned correctly
        sponsors = self.administrar_eventos.patrocinadores_evento("Test Event")
        self.assertEqual(sponsors, {"Test Sponsor": 500})

    def test_patrocinadores_evento_returns_none_when_event_does_not_exist(self):
        # Check that None is returned when the event does not exist
        sponsors = self.administrar_eventos.patrocinadores_evento("Nonexistent Event")
        self.assertIsNone(sponsors)

    def test_patrocinadores_evento_returns_none_when_event_has_no_sponsors(self):
        # Add a philanthropic event without any sponsors
        filantropico = Filantropico("Test Event", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Address", "Test City", "Open", 100, 1000)
        self.administrar_eventos.filantropicos.append(filantropico)

        # Check that None is returned when the event has no sponsors
        sponsors = self.administrar_eventos.patrocinadores_evento("Test Event")
        self.assertIsNone(sponsors)

if __name__ == '__main__':
    unittest.main()