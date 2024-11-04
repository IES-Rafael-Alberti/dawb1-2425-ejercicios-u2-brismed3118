import unittest
from unittest.mock import patch
from io import StringIO

def division(num1: float, num2: float) -> float:
    div = num1 / num2
    return div

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num2 == 0:
        print("**ERROR**")
    else:
        print(division(num1, num2))

class TestDivision(unittest.TestCase):

    def test_division_correcta(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(10, -2), -5)
        self.assertEqual(division(0, 1), 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '2'])
    def test_main_division_correcta(self, mock_input, mock_stdout):
        main()
        self.assertIn("5.0", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['10', '0'])
    def test_main_division_por_cero(self, mock_input, mock_stdout):
        main()
        self.assertIn("**ERROR**", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()