import unittest
import calculator.main.my_calculator as calc

class TestCalc(unittest.TestCase):

    def test_get_downlaod_dest_path_with_dest_file_name(self):
        self.assertEqual(25, calc.multiply(5, 5))
        self.assertEqual(10, calc.add(5, 5))
        self.assertEqual(0, calc.subtract(5, 5))
        self.assertEqual(1, calc.divide(5, 5))