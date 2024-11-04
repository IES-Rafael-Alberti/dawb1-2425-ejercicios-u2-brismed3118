import unittest
from unittest.mock import patch
from io import StringIO

def comprobar_par(num: int) -> bool:
    resto = num % 2
    return resto == 0

def main():
    num = int(input("Introduce un número entero: "))

    if num == 0:
        num = int(input("Mmm... No me sirve, prueba con otro: "))

    if comprobar_par(num):
        print("El número es par")
    else:
        print("El número es impar")

class TestComprobarPar(unittest.TestCase):

    def test_comprobar_par(self):
        self.assertTrue(comprobar_par(2))
        self.assertTrue(comprobar_par(0))
        self.assertFalse(comprobar_par(1))
        self.assertFalse(comprobar_par(-1))
        self.assertTrue(comprobar_par(-2))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['2']) 
    def test_main_numero_par(self, mock_input, mock_stdout):
        main()
        self.assertIn("El número es par", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['3']) 
    def test_main_numero_impar(self, mock_input, mock_stdout):
        main()
        self.assertIn("El número es impar", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '4']) 
    def test_main_numero_cero(self, mock_input, mock_stdout):
        main()
        self.assertIn("El número es par", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()