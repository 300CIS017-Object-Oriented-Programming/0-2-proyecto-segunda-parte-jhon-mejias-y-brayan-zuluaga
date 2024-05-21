
import unittest
from unittest.mock import Mock
from models.Teatro import Teatro
class TestTeatro(unittest.TestCase):
    def setUp(self):
        self.teatro = Teatro("Test Theater", "2023-12-31", "18:00", "20:00", "Test Venue", "Test Street", "Test City",
                             "Test State", 100)

    def test_theater_name_change(self):
        self.teatro.set_nombre("New Name")
        self.assertEqual(self.teatro.get_nombre(), "New Name")

    def test_theater_date_change(self):
        self.teatro.set_fecha("2024-01-01")
        self.assertEqual(self.teatro.get_fecha(), "2024-01-01")

    def test_theater_start_time_change(self):
        self.teatro.set_hora_inicio("19:00")
        self.assertEqual(self.teatro.get_hora_inicio(), "19:00")

    def test_theater_show_time_change(self):
        self.teatro.set_hora_show("21:00")
        self.assertEqual(self.teatro.get_hora_show(), "21:00")

    def test_theater_location_change(self):
        self.teatro.set_lugar("New Venue")
        self.assertEqual(self.teatro.get_lugar(), "New Venue")

    def test_theater_address_change(self):
        self.teatro.set_direccion("New Street")
        self.assertEqual(self.teatro.get_direccion(), "New Street")

    def test_theater_city_change(self):
        self.teatro.set_ciudad("New City")
        self.assertEqual(self.teatro.get_ciudad(), "New City")

    def test_theater_state_change(self):
        self.teatro.set_estado("New State")
        self.assertEqual(self.teatro.get_estado(), "New State")

    def test_theater_capacity_change(self):
        self.teatro.set_aforo(200)
        self.assertEqual(self.teatro.get_aforo(), 200)

    def test_theater_attendee_addition(self):
        self.teatro.agregar_asistente("Test Attendee")
        self.assertIn("Test Attendee", self.teatro.get_asistente())

    def test_artist_assignment(self):
        self.teatro.asignar_artista("Test Artist", Mock())
        self.assertIn("Test Artist", self.teatro.get_artistas())
