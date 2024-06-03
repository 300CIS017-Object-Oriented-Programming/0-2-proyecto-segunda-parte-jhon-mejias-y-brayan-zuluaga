import unittest
from models.Artista import Artista

class TestArtista(unittest.TestCase):
    def setUp(self):
        self.artista = Artista("Test Artist", "Musician")

    def test_artist_name_is_correct(self):
        self.assertEqual(self.artista.get_nombre(), "Test Artist")

    def test_artist_type_is_correct(self):
        self.assertEqual(self.artista.tipo_artista, "Musician")

    def test_artist_event_addition_is_successful(self):
        self.artista.agregar_evento("Concert", "Test Event")
        self.assertIn("Test Event", self.artista.get_eventos()["Concert"])


    def test_artist_event_retrieval_is_correct(self):
        self.artista.agregar_evento("Concert", "Test Event")
        self.assertEqual(self.artista.get_eventos(), {"Concert": ["Test Event"]})

if __name__ == '__main__':
    unittest.main()