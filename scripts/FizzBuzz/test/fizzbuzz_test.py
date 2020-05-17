import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_1_does_not_raise_value_error(self):
        assert FizzBuzz(1).number == 1
    
    def test_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-2)
    
    def test_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(101)

    def test_1_return_1(self):
        assert FizzBuzz(1).result == 1

    def test_2_return_2(self):
        assert FizzBuzz(2).result == 2

    def test_3_returns_fizz(self):
        assert FizzBuzz(3).result == "Fizz"

    def test_6_returns_buzz(self):
        assert FizzBuzz(6).result == "Fizz"
    
    def test_5_returns_buzz(self):
        assert FizzBuzz(5).result == "Buzz"

    def test_10_returns_buzz(self):
        assert FizzBuzz(10).result == "Buzz"

    def test_15_returns_fizzbuzz(self):
        assert FizzBuzz(15).result == "FizzBuzz"

    def test_30_returns_fizzbuzz(self):
        assert FizzBuzz(30).result == "FizzBuzz"

    def test_35_returns_fizzbuzz(self):
        assert FizzBuzz(35).result == "FizzBuzz"

    def test_13_returns_fizzbuzz(self):
        assert FizzBuzz(13).result == "Fizz"

    def test_50_returns_fizzbuzz(self):
        assert FizzBuzz(50).result == "Buzz"

    def test_53_returns_fizzbuzz(self):
        assert FizzBuzz(53).result == "FizzBuzz"
    
    def test_57_returns_fizzbuzz(self):
        assert FizzBuzz(57).result == "FizzBuzz"
    
    # will be useful if input range expands
    # def test_130_returns_fizzbuzz(self):
    #     assert FizzBuzz(130).result == "FizzBuzz"

