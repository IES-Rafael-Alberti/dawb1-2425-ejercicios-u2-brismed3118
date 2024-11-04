import unittest
from unittest.mock import patch
from io import StringIO

def introducir_num():
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número mayor que 1 (Introduce 0 para terminar): "))
            if num <= 1 and num != 0:
                num = None
                raise IndexError("El número debe ser mayor que 1.")
        except ValueError:
            print("*ERROR* El formato no es válido.")
        except IndexError as e:
            print(f"*ERROR* {e}")
    return num

def comprobar_primo(numeros: int):
    if numeros < 2:  
        return False

    total = 1
    for i in range(1, numeros):
        total *= i 

    total += 1

    return total % numeros == 0

def main():
    numeros = None
    primos = 0
    
    while numeros != 0:
        numeros = introducir_num()
        if numeros != 0:
            if comprobar_primo(numeros):
                primos += 1

    print(f"La cantidad de números primos introducidos es {primos}")

class TestPrimos(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', '3', '4', '5', '0'])
    def test_main(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue() 
            self.assertEqual(output.strip(), "La cantidad de números primos introducidos es 3") 
    @patch('builtins.input', side_effect=['1', '0']) 
    def test_introducir_num(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            num = introducir_num()
            self.assertEqual(num, 0)  
            self.assertIn("*ERROR* El número debe ser mayor que 1.", mock_stdout.getvalue())  

    def test_comprobar_primo(self):
        self.assertTrue(comprobar_primo(2))
        self.assertTrue(comprobar_primo(3))
        self.assertTrue(comprobar_primo(5))
        self.assertTrue(comprobar_primo(7))

        self.assertFalse(comprobar_primo(1))  
        self.assertFalse(comprobar_primo(4))
        self.assertFalse(comprobar_primo(6))
        self.assertFalse(comprobar_primo(8))
        self.assertFalse(comprobar_primo(9)) 

if __name__ == "__main__":
    unittest.main()