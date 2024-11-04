import unittest
from unittest.mock import patch
from io import StringIO

def contar_num(num: int):
    cadena = ""
    for i in range(0, num + 1):
        if i == 0:
            cadena = str(i)
        else:
            cadena = cadena + ", " + str(i)
    return cadena

def introducir_num() -> int:
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número positivo: "))
            if num < 0:
                num = None
                raise ValueError
        except ValueError:
            print("**ERROR** Algo ha ido mal, inténtalo de nuevo...")
    return num

def main():
    num = introducir_num()
    print(contar_num(num))

class TestContarNum(unittest.TestCase):

    def test_contar_num(self):
        resultado = contar_num(5)
        self.assertEqual(resultado, "0, 1, 2, 3, 4, 5") 

    @patch('builtins.input', side_effect=['-1', '3'])
    def test_introducir_num(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            num = introducir_num()
            self.assertEqual(num, 3) 
            self.assertIn("**ERROR** Algo ha ido mal, inténtalo de nuevo...", mock_stdout.getvalue()) 
    @patch('builtins.input', side_effect=['4']) 
    @patch('sys.stdout', new_callable=StringIO) 
    def test_main(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()  
        self.assertEqual(output.strip(), "0, 1, 2, 3, 4")  

if __name__ == "__main__":
    unittest.main()