import unittest
from unittest.mock import Mock
from controllers.game_controller import AdministrarEventos
from models.Asistente import Asistente
from models.Boleteria import Boleteria

class TestAdministrarEventos(unittest.TestCase):
    def setUp(self):
        self.administrar_eventos = AdministrarEventos()

    def test_vender_boletas_successful_sale(self):
        self.administrar_eventos.crear_bar("hola", "2023-12-14", "20:00", "22:00", "Lugar3", "123 Street", "Ciudad3",
                                           "Estado3", 300, 10000)
        bar = self.administrar_eventos.bares[0]  # Obtener el bar que acabamos de crear
        bar.sumar_personas = Mock()
        bar.agregar_boleteria = Mock()
        result = self.administrar_eventos.vender_boletas("Bar", "hola", "John", "Doe", 30, "123 Street",
                                                         "Internet", "preventa", "efectivo", 10)
        self.assertTrue(result)
        self.assertEqual(bar.sumar_personas.call_count, 10)
        self.assertEqual(bar.agregar_boleteria.call_count, 10)
    def test_vender_boletas_event_not_found(self):
        result = self.administrar_eventos.vender_boletas("Filantropico", "Evento No Existente", "John", "Doe", 30, "123 Street", "Internet", "preventa", "efectivo", 10)
        self.assertFalse(result)

    def test_vender_boletas_successful_sale(self):
        self.administrar_eventos.crear_bar("hola", "2023-12-14", "20:00", "22:00", "Lugar3", "123 Street",
                                           "Ciudad3",
                                           "Estado3", 300, 10000)
        bar = self.administrar_eventos.bares[0]  # Obtener el bar que acabamos de crear
        bar.sumar_personas = Mock()
        bar.agregar_boleteria = Mock()
        result = self.administrar_eventos.vender_boletas("Bar", "hola", "John", "Doe", 30, "123 Street",
                                                         "Internet", "preventa", "efectivo", 10)
        self.assertTrue(result)
        self.assertEqual(bar.sumar_personas.call_count, 10)
        self.assertEqual(bar.agregar_boleteria.call_count, 10)

    def test_vender_boletas_event_not_found(self):
        result = self.administrar_eventos.vender_boletas("Filantropico", "Evento No Existente", "John", "Doe", 30,
                                                         "123 Street", "Internet", "preventa", "efectivo", 10)
        self.assertFalse(result)

    def test_vender_boletas_event_full(self):
        # Crea un evento filantropico
        self.administrar_eventos.crear_filantropico("Evento Test", "2023-12-14", "20:00", "22:00", "Lugar3",
                                                    "123 Street", "Ciudad3", "Estado3", 100,"Patrocinador1")
        filantropico = self.administrar_eventos.filantropicos[0]  # Obtener el evento que acabamos de crear
        filantropico.get_cantidad_asistentes = Mock(return_value=100)  # Simula que el evento está lleno
        # Intenta vender boletas para un evento lleno
        result = self.administrar_eventos.vender_boletas("Filantropico", "Evento Test", "John", "Doe", 30, "123 Street",
                                                         "Internet", "preventa", "efectivo", 10)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()