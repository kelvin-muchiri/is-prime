"""Check if a number is prime."""

import unittest

def memoize(f):
    """Return memoized version of a method."""

    # Use dict to keep track of the calls
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def is_prime(num):
    """Returns true if a number is prime, false otherwise.

    Only checks upto the square root of the number. If the number
    is divisible by a number greater than its square root, it is
    also divisble by a number greater than it.

    Runtime is O(sqrt(n))"""

    if num < 2:
        return False

    i = 2

    while i * i <= num:
        if num % i == 0:
            return False

        i += 1

    return True


class TestPrimeNumber(unittest.TestCase):
    """Tests for checking if a number is prime."""

    def test_one(self):
        """Confirm that the return value for 1 is correct."""
        self.assertEqual(is_prime(1), False)

    def test_less_than_one(self):
        """Confirm that the return value for numbers less than one is correct."""
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(-1), False)

    def test_prime(self):
        """Confirm that the return value for a valid prime number is correct."""
        self.assertEqual(is_prime(5), True)

    def test_not_prime(self):
        """Confirm that the return value for an invalid prime number is correct."""
        self.assertEqual(is_prime(10), False)


if __name__ == "__main__":
    unittest.main()