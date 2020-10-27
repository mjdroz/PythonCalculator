import unittest
from Calculator import Calculator
from CSVReader import CSVReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('/csv/UnitTestAddition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result'],), )
            self.assertEqual(self.calculator.result, int(row['Result']) )

    '''def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(,), )
        self.assertEqual(self.calculator.result, )'''

if __name__ == '__main__':
    unittest.main()
