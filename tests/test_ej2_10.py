import unittest
from unittest.mock import patch
from io import StringIO

def division_num(num: int) -> bool:
    if num < 2:
        return False

    multi = 1
    for i in range(1, num):
        multi *= i

    resto = (multi + 1) % num

    return resto == 0

def obtener_num() -> int:
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número entero para ver si es primo: "))
        except ValueError:
            print("**ERROR** Ese no es un número entero")
    return num

def main():
    num = obtener_num()
    if division_num(num):
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")

class TestDivisionNum(unittest.TestCase):

    def test_division_num(self):
     
        self.assertTrue(division_num(2))  
        self.assertTrue(division_num(3)) 
        self.assertTrue(division_num(5))
        self.assertTrue(division_num(7))

        self.assertFalse(division_num(1))
        self.assertFalse(division_num(4)) 
        self.assertFalse(division_num(6)) 
        self.assertFalse(division_num(8)) 
        self.assertFalse(division_num(9)) 

    @patch('builtins.input', side_effect=['abc', '5'])
    def test_obtener_num(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            num = obtener_num()
            self.assertEqual(num, 5)
            self.assertIn("**ERROR** Ese no es un número entero", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['11'])
    @patch('sys.stdout', new_callable=StringIO)  
    def test_main(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue() 
        self.assertEqual(output.strip(), "El número 11 es primo")

if __name__ == "__main__":
    unittest.main()