import pytest
from app.calculator import Calculator

class TestCalc
    def setup(self):
        self.calc = Calculator

    def multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def division(self):
        assert self.calc.division(self, 6, 3) == 2

    def subtraction(self):
        assert self.calc.subtraction(self, 4, 3) == 2

    def adding(self):
        assert self.calc.adding(self, 1, 3)

    def teardown(self):
        print( 'TearDown выполнен')