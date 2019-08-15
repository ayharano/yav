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
    YAVPatternMatchError,
    YAVOutOfBoundariesError,
    YAVRepeatedDigitApartedByOneError,
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

        for invalid_match_instance in (
                '123.456',
                '987,654',
                'cent vingt trois mil cinq cent soixant-sept'
        ):

            with self.subTest(value=invalid_match_instance):
                with self.assertRaisesRegex(
                        YAVPatternMatchError,
                        r"{0} expected to be a str composed by "
                        r"a sequence of six ASCII digits"
                        .format(re.escape(str(invalid_match_instance))),
                        msg="{0} should raise an Exception"
                        .format(invalid_match_instance),
                ):
                    self.validator(value=invalid_match_instance)

    def test_input_int_out_of_boundaries(self):
        """Verify if int input is within expected boundaries."""

        for out_of_boundaries_int in (
                -42,
                0,
                42,
                99999,
                100000,
                999999,
                1000000,
                1234567,
        ):

            with self.subTest(value=out_of_boundaries_int):
                with self.assertRaisesRegex(
                        YAVOutOfBoundariesError,
                        r"{0} is an int parameter but should be"
                        r" between 100000 \(exclusive\) and"
                        r" 999999 \(exclusive\)"
                        .format(out_of_boundaries_int),
                        msg="{0} should raise an Exception"
                        .format(out_of_boundaries_int),
                ):
                    self.validator(value=out_of_boundaries_int)

    def test_input_repeated_digit_aparted_by_one_int_values(self):
        """int input which should not pass because of repetition rule."""

        for repeated_digit_aparted_by_one_int in (
                121426,
                552523,
        ):

            with self.subTest(value=repeated_digit_aparted_by_one_int):
                with self.assertRaisesRegex(
                        YAVRepeatedDigitApartedByOneError,
                        r"{0} should not have a repeated digit"
                        r" aparted by one digit"
                        r" \(e\.g\. 12145 and 12325\)"
                        .format(repeated_digit_aparted_by_one_int),
                        msg="{0} should raise an Exception"
                        .format(repeated_digit_aparted_by_one_int),
                ):
                    self.validator(value=repeated_digit_aparted_by_one_int)

    def test_input_repeated_digit_aparted_by_one_str_values(self):
        """str input which should not pass because of apart repeated rule."""

        for repeated_digit_aparted_by_one_str in (
                '121426',
                '552523',
        ):

            with self.subTest(value=repeated_digit_aparted_by_one_str):
                with self.assertRaisesRegex(
                        YAVRepeatedDigitApartedByOneError,
                        r"{0} should not have a repeated digit"
                        r" aparted by one digit"
                        r" \(e\.g\. 12145 and 12325\)"
                        .format(repeated_digit_aparted_by_one_str),
                        msg="{0} should raise an Exception"
                        .format(repeated_digit_aparted_by_one_str),
                ):
                    self.validator(value=repeated_digit_aparted_by_one_str)

    def test_input_expected_int_values(self):
        """int values which should pass."""

        for valid_int in (
                523563,
                112233,
        ):
            with self.subTest(value=valid_int):
                self.assertIsNone(
                    self.validator(value=valid_int),
                    msg="{0} should be a valid parameter"
                    .format(valid_int)
                )

    def test_input_expected_str_values(self):
        """str values which should pass."""

        for valid_str in (
                '523563',
                '112233',
        ):
            with self.subTest(value=valid_str):
                self.assertIsNone(
                    self.validator(value=valid_str),
                    msg="{0} should be a valid parameter"
                    .format(valid_str)
                )
