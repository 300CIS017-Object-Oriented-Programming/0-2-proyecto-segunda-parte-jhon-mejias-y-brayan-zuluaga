import unittest
from models.Boleteria import Boleteria

class TestBoleteria(unittest.TestCase):
    def setUp(self):
        self.boleteria = Boleteria("Regular", 100, 150, "Credit Card")

    def test_boleteria_type(self):
        self.assertEqual(self.boleteria.get_tipo_boleteria(), "Regular")

    def test_boleteria_preventa_price(self):
        self.assertEqual(self.boleteria.get_precio_preventa(), 100)

    def test_boleteria_regular_price(self):
        self.assertEqual(self.boleteria.get_precio_regular(), 150)

    def test_boleteria_payment_method(self):
        self.assertEqual(self.boleteria.get_metodo_pago(), "Credit Card")

    def test_boleteria_price_change(self):
        self.boleteria.set_precios(120, 180)
        self.assertEqual(self.boleteria.get_precio_preventa(), 120)
        self.assertEqual(self.boleteria.get_precio_regular(), 180)

if __name__ == '__main__':
    unittest.main()