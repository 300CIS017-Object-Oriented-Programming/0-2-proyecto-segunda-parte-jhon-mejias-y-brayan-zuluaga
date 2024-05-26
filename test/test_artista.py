import unittest
from models.Artista import Artista
from unittest.mock import MagicMock
from controllers.game_controller import AdministrarEventos
class TestArtista(unittest.TestCase):
    #def setUp(self):

       #self.artista = Artista("Test Artist", "Musician")

    def setUp(self):
        self.administrar_eventos = AdministrarEventos()
    def test_artist_name(self):
        self.assertEqual(self.artista.getNombre(), "Test Artist")

    def test_artist_event_addition(self):
        self.artista.agregarNombreEvento("Test Event")
        self.assertIn("Test Event", self.artista.getNombreEventos())



    def test_asignar_artista_to_bar_event_successfully(self):
        self.administrar_eventos.bares = [MagicMock()]
        self.administrar_eventos.bares[0].get_nombre.return_value = "Bar Event"
        self.administrar_eventos.artistas = {"Artist Name": MagicMock()}

        result = self.administrar_eventos.asignar_artista("bar", "Bar Event", "Artist Name")

        self.assertEqual(result, True)

    def test_asignar_artista_to_teatro_event_successfully(self):
        self.administrar_eventos.teatros = [MagicMock()]
        self.administrar_eventos.teatros[0].get_nombre.return_value = "Teatro Event"
        self.administrar_eventos.artistas = {"Artist Name": MagicMock()}

        result = self.administrar_eventos.asignar_artista("teatro", "Teatro Event", "Artist Name")

        self.assertEqual(result, True)

    def test_asignar_artista_to_filantropico_event_successfully(self):
        self.administrar_eventos.filantropicos = [MagicMock()]
        self.administrar_eventos.filantropicos[0].get_nombre.return_value = "Filantropico Event"
        self.administrar_eventos.artistas = {"Artist Name": MagicMock()}

        result = self.administrar_eventos.asignar_artista("filantropico", "Filantropico Event", "Artist Name")

        self.assertEqual(result, True)

    def test_asignar_nonexistent_artist_to_event(self):
        self.administrar_eventos.bares = [MagicMock()]
        self.administrar_eventos.bares[0].get_nombre.return_value = "Bar Event"
        self.administrar_eventos.artistas = {}

        result = self.administrar_eventos.asignar_artista("bar", "Bar Event", "Nonexistent Artist")

        self.assertEqual(result, False)

    def test_asignar_artist_to_nonexistent_event(self):
        self.administrar_eventos.bares = []
        self.administrar_eventos.artistas = {"Artist Name": MagicMock()}

        result = self.administrar_eventos.asignar_artista("bar", "Nonexistent Event", "Artist Name")

        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()