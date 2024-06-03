import unittest
from unittest.mock import Mock
from models.Bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Test Bar", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City",
                       "Test State", 100, 5000)

    def test_bar_name_change(self):
        self.bar.set_nombre("New Name")
        self.assertEqual(self.bar.get_nombre(), "New Name")

    def test_bar_date_change(self):
        self.bar.set_fecha("2024-01-01")
        self.assertEqual(self.bar.get_fecha(), "2024-01-01")

    def test_bar_start_time_change(self):
        self.bar.set_hora_inicio("19:00")
        self.assertEqual(self.bar.get_hora_inicio(), "19:00")

    def test_bar_show_time_change(self):
        self.bar.set_hora_show("21:00")
        self.assertEqual(self.bar.get_hora_show(), "21:00")

    def test_bar_location_change(self):
        self.bar.set_lugar("New Venue")
        self.assertEqual(self.bar.get_lugar(), "New Venue")

    def test_bar_address_change(self):
        self.bar.set_direccion("New Street")
        self.assertEqual(self.bar.get_direccion(), "New Street")

    def test_bar_city_change(self):
        self.bar.set_ciudad("New City")
        self.assertEqual(self.bar.get_ciudad(), "New City")

    def test_bar_state_change(self):
        self.bar.set_estado("New State")
        self.assertEqual(self.bar.get_estado(), "New State")

    def test_bar_capacity_change(self):
        self.bar.set_aforo(200)
        self.assertEqual(self.bar.get_aforo(), 200)

    def test_bar_attendee_addition(self):
        self.bar.agregar_asistente("Test Attendee")
        self.assertIn("Test Attendee", self.bar.get_asistente())

    def test_artist_assignment(self):
        self.bar.asignar_artista("Test Artist", Mock())
        self.assertIn("Test Artist", self.bar.get_artistas())

if __name__ == '__main__':
    unittest.main()