import unittest
from controllers.gui_controller import GuiController

class GuiControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = GuiController()

    def test_activation_creando_evento_changes_state(self):
        self.controller.activate_creando_evento()
        self.assertTrue(self.controller.get_creando_evento())

    def test_desactivation_creando_evento_changes_state(self):
        self.controller.activate_creando_evento()
        self.controller.desactivate_creando_evento()
        self.assertFalse(self.controller.get_creando_evento())

    def test_activation_editando_evento_changes_state(self):
        self.controller.activate_editando_evento()
        self.assertTrue(self.controller.get_editando_evento())

    def test_desactivation_editando_evento_changes_state(self):
        self.controller.activate_editando_evento()
        self.controller.desactivate_editando_evento()
        self.assertFalse(self.controller.get_editando_evento())

    def test_activation_eliminando_evento_changes_state(self):
        self.controller.activate_eliminando_evento()
        self.assertTrue(self.controller.get_eliminando_evento())

    def test_desactivation_eliminando_evento_changes_state(self):
        self.controller.activate_eliminando_evento()
        self.controller.desactivate_eliminando_evento()
        self.assertFalse(self.controller.get_eliminando_evento())

    def test_activation_generando_reportes_changes_state(self):
        self.controller.activate_generando_reportes()
        self.assertTrue(self.controller.get_generando_reportes())

    def test_desactivation_generando_reportes_changes_state(self):
        self.controller.activate_generando_reportes()
        self.controller.desactivate_generando_reportes()
        self.assertFalse(self.controller.get_generando_reportes())

    def test_activation_vendiendo_boletas_changes_state(self):
        self.controller.activate_vendiendo_boletas()
        self.assertTrue(self.controller.get_vendiendo_boletas())

    def test_desactivation_vendiendo_boletas_changes_state(self):
        self.controller.activate_vendiendo_boletas()
        self.controller.desactivate_vendiendo_boletas()
        self.assertFalse(self.controller.get_vendiendo_boletas())

    def test_activation_creando_artista_changes_state(self):
        self.controller.activate_creando_artista()
        self.assertTrue(self.controller.get_creando_artista())

    def test_desactivation_creando_artista_changes_state(self):
        self.controller.activate_creando_artista()
        self.controller.desactivate_creando_artista()
        self.assertFalse(self.controller.get_creando_artista())

    def test_activation_asignando_artista_changes_state(self):
        self.controller.activate_asignando_artista()
        self.assertTrue(self.controller.get_asignando_artista())

    def test_desactivation_asignando_artista_changes_state(self):
        self.controller.activate_asignando_artista()
        self.controller.desactivate_asignando_artista()
        self.assertFalse(self.controller.get_asignando_artista())

    def test_activation_mostrando_detalles_evento_changes_state(self):
        self.controller.activate_mostrando_detalles_evento()
        self.assertTrue(self.controller.get_mostrando_detalles_evento())

    def test_desactivation_mostrando_detalles_evento_changes_state(self):
        self.controller.activate_mostrando_detalles_evento()
        self.controller.desactivate_mostrando_detalles_evento()
        self.assertFalse(self.controller.get_mostrando_detalles_evento())

    def test_activation_imprimiendo_eventos_changes_state(self):
        self.controller.activate_imprimiendo_eventos()
        self.assertTrue(self.controller.get_imprimiendo_eventos())

    def test_desactivation_imprimiendo_eventos_changes_state(self):
        self.controller.activate_imprimiendo_eventos()
        self.controller.desactivate_imprimiendo_eventos()
        self.assertFalse(self.controller.get_imprimiendo_eventos())

    def test_activation_registrar_ingreso_changes_state(self):
        self.controller.activate_registrar_ingreso()
        self.assertTrue(self.controller.get_registrar_ingreso())

    def test_desactivation_registrar_ingreso_changes_state(self):
        self.controller.activate_registrar_ingreso()
        self.controller.desactivate_registrar_ingreso()
        self.assertFalse(self.controller.get_registrar_ingreso())

if __name__ == '__main__':
    unittest.main()