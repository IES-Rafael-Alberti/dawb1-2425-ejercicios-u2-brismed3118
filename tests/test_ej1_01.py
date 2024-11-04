import unittest
from unittest.mock import patch
from io import StringIO

def comprobar_edad(edad: int) -> bool:
    if edad >= 18:
        return True
    else:
        return False

def main():
    edad = int(input("Introduce tu edad: "))
    if comprobar_edad(edad) == True:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

class TestComprobarEdad(unittest.TestCase):

    def test_mayor_de_edad(self):
        self.assertTrue(comprobar_edad(18))
        self.assertTrue(comprobar_edad(25))
        self.assertTrue(comprobar_edad(100))

    def test_menor_de_edad(self):
        self.assertFalse(comprobar_edad(17))
        self.assertFalse(comprobar_edad(0))
        self.assertFalse(comprobar_edad(10))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['20'])
    def test_main_mayor_de_edad(self, mock_input, mock_stdout):
        main()
        self.assertIn("Eres mayor de edad", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['15'])
    def test_main_menor_de_edad(self, mock_input, mock_stdout):
        main()
        self.assertIn("Eres menor de edad", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()