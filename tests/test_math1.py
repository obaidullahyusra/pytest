# Multiplication test ideas:
# two positive integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats
# --------------------------------------------------------------------------------
# A parametrized test function
# --------------------------------------------------------------------------------
import pytest
products = [
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product