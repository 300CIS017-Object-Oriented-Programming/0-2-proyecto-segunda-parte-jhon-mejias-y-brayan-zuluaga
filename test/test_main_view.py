import unittest
from unittest.mock import MagicMock
from view.main_view import View

class TestView(unittest.TestCase):
    def setUp(self):
        self.view = View()

    def test_generate_key(self):
        base_key = "test_key"
        generated_key = self.view.generate_key(base_key)
        self.assertEqual(generated_key, "test_key_0")

    def test_generate_key_increment(self):
        base_key = "test_key"
        self.view.generate_key(base_key)
        generated_key = self.view.generate_key(base_key)
        self.assertEqual(generated_key, "test_key_1")



if __name__ == '__main__':
    unittest.main()