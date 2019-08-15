# MIT License

# Copyright (c) 2019 Alexandre Yukio Harano

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Basic test cases for yav."""
from unittest import TestCase

from yav import (
    YAValidator,
    YAVInputTypeError,
    YAVOutOfBoundariesError,
    YAVRepetitiveDigitsError,
)


class TestInputOutput(TestCase):
    """Basic test cases for pair of expected input/output."""
    def setUp(self):
        """Cases setup method."""
        pass

    def tearDown(self):
        """Cases finally like method."""
        pass

    def test_input_invalid_type(self):
        """Only int and str are expected."""
        pass

    def test_input_invalid_str(self):
        """str are valid input if expected pattern matches."""
        pass

    def test_input_str_out_of_boundaries(self):
        """Verify if str input is within expected boundaries."""
        pass

    def test_input_int_out_of_boundaries(self):
        """Verify if int input is within expected boundaries."""
        pass

    def test_input_expected_int_values(self):
        """int values which should pass."""
        pass

    def test_input_expected_str_values(self):
        """str values which should pass."""
        pass
