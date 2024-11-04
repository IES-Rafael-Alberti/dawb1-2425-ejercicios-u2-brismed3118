import unittest
from unittest.mock import patch
from io import StringIO

def calcular_precio(edad: int):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10
    
def introducir_edad():
    edad = None

    while edad is None:
        try:
            edad = int(input("Por favor, introduce la edad del cliente: "))
        except ValueError:
            print("Esa edad no es válida")
            edad = None

    return edad 

def main():
    edad = introducir_edad()
    precio = calcular_precio(edad)
    print(f"El precio de la entrada es: {precio}€")

class TestCalcularPrecio(unittest.TestCase):

    def test_calcular_precio(self):
        self.assertEqual(calcular_precio(3), 0) 
        self.assertEqual(calcular_precio(4), 5) 
        self.assertEqual(calcular_precio(10), 5) 
        self.assertEqual(calcular_precio(18), 5) 
        self.assertEqual(calcular_precio(19), 10) 
        self.assertEqual(calcular_precio(65), 10) 

    @patch('builtins.input', side_effect=['abc', '5']) 
    def test_introducir_edad(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            edad = introducir_edad()
            self.assertEqual(edad, 5)
            self.assertIn("Esa edad no es válida", mock_stdout.getvalue()) 

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10']) 
    def test_main(self, mock_input, mock_stdout):
        main()
        self.assertIn("El precio de la entrada es: 5€", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()