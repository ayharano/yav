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

from typing import Union


class BaseYAVException(Exception):
    """All yav Exceptions should be derived from this."""
    pass


class YAVInputTypeError(BaseYAVException):
    """Exception for invalid input type."""
    pass


class YAVOutOfBoundariesError(BaseYAVException):
    """Exception for input out of rules' boundaries."""
    pass


class YAVRepetitiveDigitsError(BaseYAVException):
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
            YAVOutOfBoundariesError:
                Content value outside of expected boundaries.
            YAVRepetitiveDigitsError:
                Repetitive digits found in content value.
        """

        if not isinstance(value, (int, str)):
            raise YAVInputTypeError(
                "{0} should be either an int or str"
                .format(value)
            )
