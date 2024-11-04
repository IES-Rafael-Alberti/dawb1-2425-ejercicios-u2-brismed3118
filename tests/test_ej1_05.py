import unittest
from unittest.mock import patch
from io import StringIO

def tributa(edad: int, salario: int) -> bool:
    if edad > 16 and salario >= 1000:
        return True
    else:
        return False

def main():
    edad = None
    salario = None

    while edad is None or salario is None:
        try:
            edad = int(input("Introduzca su edad: "))
            salario = int(input("Introduzca su salario mensual: "))
        except ValueError:
            print("**ERROR** Edad o salario no válidos")

    if tributa(edad, salario):
        print("Tributa")
    else:
        print("No tributa")

class TestTributa(unittest.TestCase):

    def test_tributa(self):
        self.assertTrue(tributa(17, 1000)) 
        self.assertTrue(tributa(30, 1500)) 
        self.assertFalse(tributa(16, 1000)) 
        self.assertFalse(tributa(17, 500)) 
        self.assertFalse(tributa(15, 1500)) 
        self.assertFalse(tributa(0, 1000)) 
        self.assertFalse(tributa(20, 0)) 

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['20', '1500']) 
    def test_main_tributa(self, mock_input, mock_stdout):
        main()
        self.assertIn("Tributa", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['15', '500']) 
    def test_main_no_tributa(self, mock_input, mock_stdout):
        main()
        self.assertIn("No tributa", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['abc', '500', '20', '1500']) 
    def test_main_error_input(self, mock_input, mock_stdout):
        main()
        self.assertIn("**ERROR** Edad o salario no válidos", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()