import unittest
from models.Artista import Artista

class TestArtista(unittest.TestCase):
    def setUp(self):
        self.artista = Artista("Test Artist", "Musician")

    def test_artist_name(self):
        self.assertEqual(self.artista.getNombre(), "Test Artist")

    def test_artist_event_addition(self):
        self.artista.agregarNombreEvento("Test Event")
        self.assertIn("Test Event", self.artista.getNombreEventos())

if __name__ == '__main__':
    unittest.main()