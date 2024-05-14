import unittest
from models.Filantropico import Filantropico
from models.Teatro import Teatro
from models.Bar import Bar

class TestEventCreation(unittest.TestCase):
    def test_crear_evento_filantropico(self):
        # Crear una instancia de Filantropico
        filantropico = Filantropico("Evento1", "2023-12-12", "18:00", "20:00", "Lugar1", "Direccion1", "Ciudad1",
                                    "Estado1", 100)
        # Verificar que la instancia se ha creado correctamente
        self.assertEqual(filantropico.get_nombre(), "Evento1")

    def test_crear_evento_teatro(self):
        # Crear una instancia de Teatro
        teatro = Teatro("Evento2", "2023-12-13", "19:00", "21:00", "Lugar2", "Direccion2", "Ciudad2", "Estado2", 200)
        # Verificar que la instancia se ha creado correctamente
        self.assertEqual(teatro.get_nombre(), "Evento2")

    def test_crear_evento_bar(self):
        # Crear una instancia de Bar
        bar = Bar("Evento3", "2023-12-14", "20:00", "22:00", "Lugar3", "Direccion3", "Ciudad3", "Estado3", 300, 10000)
        # Verificar que la instancia se ha creado correctamente
        self.assertEqual(bar.get_nombre(), "Evento3")

if __name__ == '__main__':
    unittest.main()