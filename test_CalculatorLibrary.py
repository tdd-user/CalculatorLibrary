"""
Unit tests for the calculator library
"""

import CalculatorLibrary


class TestCalculator:

    def test_addition(self):
        assert 4 == CalculatorLibrary.add(2, 2)

    def test_subtraction(self):
        assert 2 == CalculatorLibrary.subtract(4, 2)
