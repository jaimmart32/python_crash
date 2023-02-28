import unittest
from survey import AnonymousSurvey

# el metodo setUp()de TestCase crea un objeto que estará disponible en todos los métodos de prueba que escribamos.

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey."""

    def setUp(self):
        """Crea una encuesta y un conjunto de repuestas para usar en todos los métodos de prueba."""
        question = "What color is your Bugatti?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['gold', 'copper', 'green']

    def test_store_single_response(self):
        """Comprueba si una respuesta simple se guarda bien."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Comprueba que se guardan correctamente tres respuestas individuales."""
        
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()