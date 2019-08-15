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
"""yav's package core implementation."""

from itertools import starmap
import re
from typing import Union


class BaseYAVException(Exception):
    """All yav Exceptions should be derived from this."""
    pass


class YAVInputTypeError(BaseYAVException):
    """Exception for invalid input type."""
    pass


class YAVPatternMatchError(BaseYAVException):
    """Exception for invalid pattern for str input."""
    pass


class YAVOutOfBoundariesError(BaseYAVException):
    """Exception for input out of rules' boundaries."""
    pass


class YAVRepeatedDigitApartedByOneError(BaseYAVException):
    """Exception for specific rule about content values."""
    pass


class YAValidator:
    """Custom hardcoded set of rules validator."""

    def __call__(self, value: Union[int, str]) -> None:
        """Raises a BaseYAVException if not valid, None otherwise.

        Args:
            value: value to be validated against rules.

        Raises:
            YAVInputTypeError:
                Invalid input type.
            YAVPatternMatchError:
                Invalid pattern for str input.
            YAVOutOfBoundariesError:
                Content value outside of expected boundaries.
            YAVRepeatedDigitApartedByOneError:
                Repetitive digits found in content value.
        """

        if not isinstance(value, (int, str)):
            raise YAVInputTypeError(
                "{0} should be either an int or str"
                .format(value)
            )

        if isinstance(value, str):
            if not re.search(r'[1-9][0-9]{5}', str(value)):
                raise YAVPatternMatchError(
                    "{0} expected to be a str composed by "
                    "a sequence of six ASCII digits"
                    .format(value)
                )

        value_as_int = int(value)

        if value_as_int <= 100000 or value_as_int >= 999999:
            raise YAVOutOfBoundariesError(
                "{0} is an int parameter but should be "
                "between 100000 (exclusive) and 999999 (exclusive)"
                .format(value_as_int)
            )

        value_as_str = str(value)

        # Actual repeated digit validator for one pair of digits
        pair_validator = lambda one, another: one != another

        # Actual pair validation:
        # applies to every pair of digits aparted by one digit,
        # returning True if all pairs are validated
        all_pairs_validated = all(
            list(
                starmap(
                    pair_validator,
                    zip(
                        value_as_str[0:4:1],
                        value_as_str[2:6:1],
                    )
                )
            )
        )

        if not all_pairs_validated:
            raise YAVRepeatedDigitApartedByOneError(
                "{0} should not have a repeated digit aparted by"
                " one digit (e.g. 12145 and 12325)"
                .format(value_as_str)
            )
