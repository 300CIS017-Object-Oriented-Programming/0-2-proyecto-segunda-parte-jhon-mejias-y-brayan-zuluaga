import unittest
from unittest.mock import Mock
from models.Filantropico import Filantropico

class TestFilantropico(unittest.TestCase):
    def setUp(self):
        self.filantropico = Filantropico("Test Filantropico", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City", "Test State", 100, 5000)

    def test_filantropico_name_change(self):
        self.filantropico.set_nombre("New Name")
        self.assertEqual(self.filantropico.get_nombre(), "New Name")

    def test_filantropico_date_change(self):
        self.filantropico.set_fecha("2024-01-01")
        self.assertEqual(self.filantropico.get_fecha(), "2024-01-01")

    def test_filantropico_start_time_change(self):
        self.filantropico.set_hora_inicio("19:00")
        self.assertEqual(self.filantropico.get_hora_inicio(), "19:00")

    def test_filantropico_show_time_change(self):
        self.filantropico.set_hora_show("21:00")
        self.assertEqual(self.filantropico.get_hora_show(), "21:00")

    def test_filantropico_location_change(self):
        self.filantropico.set_lugar("New Venue")
        self.assertEqual(self.filantropico.get_lugar(), "New Venue")

    def test_filantropico_address_change(self):
        self.filantropico.set_direccion("New Street")
        self.assertEqual(self.filantropico.get_direccion(), "New Street")

    def test_filantropico_city_change(self):
        self.filantropico.set_ciudad("New City")
        self.assertEqual(self.filantropico.get_ciudad(), "New City")

    def test_filantropico_state_change(self):
        self.filantropico.set_estado("New State")
        self.assertEqual(self.filantropico.get_estado(), "New State")

    def test_filantropico_capacity_change(self):
        self.filantropico.set_aforo(200)
        self.assertEqual(self.filantropico.get_aforo(), 200)

    def test_filantropico_attendee_addition(self):
        self.filantropico.agregar_asistente("Test Attendee")
        self.assertIn("Test Attendee", self.filantropico.get_asistente())

    def test_artist_assignment(self):
        self.filantropico.asignar_artista("Test Artist", Mock())
        self.assertIn("Test Artist", self.filantropico.get_artistas())

    def test_patrocinador_addition(self):
        self.filantropico.asignar_patrocinador("Test Sponsor",2300)
        self.assertIn("Test Sponsor", self.filantropico.patrocinadores)

if __name__ == '__main__':
    unittest.main()