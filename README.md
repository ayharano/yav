# Yet Another Validator

![GitHub](https://img.shields.io/github/license/ayharano/yav?style=for-the-badge)

> Yet Another Validator for a specific hardcoded set of rules.

## Installation and usage

### Installation

After cloning this repo, *yav* can be installed in the root directory by running
`pip install -e . yav`. It requires Python 3.5.0+.


### Usage

To use *yav*:

```
yav to_be_validated [to_be_validated ...]
```

### Command line options

*yav* has no option besides help:

```text
yav [-h] to_be_validated [to_be_validated ...]

__   __   _
\ \ / /__| |_
 \ V / _ \ __|
  | |  __/ |_
  |_|\___|\__|

             _                _   _
            / \   _ __   ___ | |_| |__   ___ _ __
           / _ \ | '_ \ / _ \| __| '_ \ / _ \ '__|
          / ___ \| | | | (_) | |_| | | |  __/ |
         /_/   \_\_| |_|\___/ \__|_| |_|\___|_|

                __     __    _ _     _       _
                \ \   / /_ _| (_) __| | __ _| |_ ___  _ __
                 \ \ / / _` | | |/ _` |/ _` | __/ _ \| '__|
                  \ V / (_| | | | (_| | (_| | || (_) | |
                   \_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|

Yet Another Validator is a command line interface to validate
if each given parameter is valid against the following rules:

 (i) an integer bigger than 100_000 and smaller than 999_999, and

 (ii) digits cannot be repeated aparted by one digit (e.g.: 12145; 12325).

positional arguments:
  to_be_validated  One or more parameters to be validated against rules

optional arguments:
  -h, --help       show this help message and exit
```
