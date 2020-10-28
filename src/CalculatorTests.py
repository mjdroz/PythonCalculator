import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('/src/UnitTestAddition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CSVReader('/src/UnitTestSubtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result,int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data = CSVReader('/src/UnitTestMultiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result,int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CSVReader('/src/UnitTestDivision.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CSVReader('/src/UnitTestSquare.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_squareRoot_method_calculator(self):
        test_data = CSVReader('/src/UnitTestSquareRoot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareRoot(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

if __name__ == '__main__':
    unittest.main()
