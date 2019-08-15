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
import re
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
        self.validator = YAValidator()

    def tearDown(self):
        """Cases finally like method."""
        pass

    def test_input_invalid_type(self):
        """Only int and str are expected."""

        for invalid_type_instance in (
                0.,
                0.j,
                [],
                (),
                range(0),
                set({}),
                frozenset({}),
                {},
                None,
        ):

            with self.subTest(value=invalid_type_instance):
                with self.assertRaisesRegex(
                        YAVInputTypeError,
                        r"{0} should be either an int or str"
                        .format(re.escape(str(invalid_type_instance))),
                        msg="{0} should raise an Exception"
                        .format(invalid_type_instance),
                ):
                    self.validator(value=invalid_type_instance)

    def test_input_invalid_str(self):
        """str are valid input if expected pattern matches."""
        pass

    def test_input_str_out_of_boundaries(self):
        """Verify if str input is within expected boundaries."""

        for out_of_boundaries_str in (
                '0',
                '42',
                '999999',
                '1000000',
                '1234567',
        ):

            with self.subTest(value=out_of_boundaries_str):
                with self.assertRaisesRegex(
                        YAVOutOfBoundariesError,
                        r"{0} is an int parameter but should be "
                        r"between 100000 \(inclusive\) and 999999 \(exclusive\)"
                        .format(out_of_boundaries_str),
                        msg="{0} should raise an Exception"
                        .format(out_of_boundaries_str),
                ):
                    self.validator(value=out_of_boundaries_str)

    def test_input_int_out_of_boundaries(self):
        """Verify if int input is within expected boundaries."""

        for out_of_boundaries_int in (
                -42,
                0,
                42,
                999999,
                1000000,
                1234567,
        ):

            with self.subTest(value=out_of_boundaries_int):
                with self.assertRaisesRegex(
                        YAVOutOfBoundariesError,
                        r"{0} is an int parameter but should be "
                        r"between 100000 \(inclusive\) and 999999 \(exclusive\)"
                        .format(out_of_boundaries_int),
                        msg="{0} should raise an Exception"
                        .format(out_of_boundaries_int),
                ):
                    self.validator(value=out_of_boundaries_int)

    def test_input_expected_int_values(self):
        """int values which should pass."""
        pass

    def test_input_expected_str_values(self):
        """str values which should pass."""
        pass
