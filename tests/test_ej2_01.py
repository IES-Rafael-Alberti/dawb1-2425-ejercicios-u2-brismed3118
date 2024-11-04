import unittest
from unittest.mock import patch
from io import StringIO

def repetir_palabra(palabra: str):
    for i in range(10):
        print(palabra)

def introducir_palabra() -> str:
    palabra = None
    while palabra is None:
        try:
            palabra = input("Introduce la palabra que quieras: ")
            if palabra == "":
                palabra = None
                raise ValueError
        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return palabra

def main():
    palabra = introducir_palabra()
    repetir_palabra(palabra)

class TestRepetirPalabra(unittest.TestCase):

    @patch('builtins.input', side_effect=['Hola']) 
    @patch('sys.stdout', new_callable=StringIO)  
    def test_repetir_palabra(self, mock_stdout, mock_input):
        palabra = introducir_palabra()  
        repetir_palabra(palabra) 
        output = mock_stdout.getvalue().strip().split('\n') 
        self.assertEqual(len(output), 10)  
        self.assertEqual(output[0], "Hola") 

    @patch('builtins.input', side_effect=['', 'Hola']) 
    def test_introducir_palabra(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            palabra = introducir_palabra()
            self.assertEqual(palabra, "Hola")  
            self.assertIn("**ERROR** Algo ha ido mal, inténtalo de nuevo...", mock_stdout.getvalue()) 

    @patch('builtins.input', side_effect=['Hola']) 
    @patch('sys.stdout', new_callable=StringIO) 
    def test_main(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue().strip().split('\n') 
        self.assertEqual(len(output), 10) 
        self.assertEqual(output[0], "Hola") 

if __name__ == "__main__":
    unittest.main()