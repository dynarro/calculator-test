import unittest
import sys
import mock
import shutil, tempfile
from os import path
from mock import Mock
from calculations import addition, substraction, multiplication, division, get_values, int_input


class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(4, addition(2,2))
        self.assertEqual(3.2, addition(1,2.2))

    def test_substraction(self):
        self.assertEqual(2, substraction(3,1))
        self.assertEqual(-2, substraction(1,3))

    def test_multiplication(self):
        self.assertEqual(12, multiplication(3,4))
        self.assertEqual(13.5, multiplication(3,4.5))

    def test_division(self):
        self.assertEqual(3, division(9,3))
        self.assertRaises(ZeroDivisionError, division, 3,0)

    def test_get_values(self):
        # Mocks two values to use for the test as raw_input values.
        with mock.patch('__builtin__.raw_input') as mri:
            mri.side_effect = ['2','3']
            first_value, second_value = get_values(interactive=True)
            self.assertEqual(2, first_value)
            self.assertEqual(3, second_value)

        # Create a temporary directory
            self.test_dir = tempfile.mkdtemp()

        # Create a file in the temporary directory
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        # Write something to it
        f.write('Foo')
        # Reopen the file and check if what we read back is the same
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(f.read(),'Foo')
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
