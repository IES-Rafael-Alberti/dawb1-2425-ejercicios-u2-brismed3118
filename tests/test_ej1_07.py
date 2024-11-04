import unittest
from unittest.mock import patch
from io import StringIO

def comprobar_tramo(renta: float):
    if renta < 10000:
        print("El tio de impositivo es 5%")
    if renta >= 10000 and renta < 20000:
        print("El tio de impositivo es 15%")
    if renta >= 20000 and renta < 35000:
        print("El tio de impositivo es 20%")
    if renta >= 35000 and renta < 60000:
        print("El tio de impositivo es 30%")
    if renta >= 60000:
        print("El tio de impositivo es 45%")   

def main():
    renta = None

    while renta is None:
        try:
            renta = float(input("Introduzca su renta anual: "))
            if renta < 0:
                renta = None
                raise ValueError
        except ValueError:
            print("**ERROR** Esa no es una renta válida...")
            renta = None

    comprobar_tramo(renta)

class TestComprobarTramo(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_tramo_5(self, mock_stdout):
        comprobar_tramo(5000)
        self.assertIn("El tio de impositivo es 5%", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_tramo_15(self, mock_stdout):
        comprobar_tramo(15000)
        self.assertIn("El tio de impositivo es 15%", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_tramo_20(self, mock_stdout):
        comprobar_tramo(25000)
        self.assertIn("El tio de impositivo es 20%", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_tramo_30(self, mock_stdout):
        comprobar_tramo(45000)
        self.assertIn("El tio de impositivo es 30%", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_comprobar_tramo_45(self, mock_stdout):
        comprobar_tramo(60000)
        self.assertIn("El tio de impositivo es 45%", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['-5000', 'abc', '10000']) 
    def test_main_invalid_input(self, mock_input, mock_stdout):
        main()
        self.assertIn("**ERROR** Esa no es una renta válida...", mock_stdout.getvalue())
        self.assertIn("El tio de impositivo es 15%", mock_stdout.getvalue()) 

if __name__ == "__main__":
    unittest.main()