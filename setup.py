from pathlib import Path

from setuptools import setup, find_packages


# Based on PyPA's sampleproject located at https://github.com/pypa/sampleproject


PROJECT_NAME = 'yav'


here = Path(__file__).parent
readme_path = here / 'README.md'
version_path = here / PROJECT_NAME / 'VERSION'


with readme_path.open(encoding='utf-8') as r:
    long_description = r.read()


with version_path.open(encoding='utf-8') as v:
    version = v.read()


setup(
    name=PROJECT_NAME,

    version=version,

    description='Yet Another Validator for a specific hardcoded set of rules',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ayharano/yav',

    author='Alexandre Yukio Harano',

    author_email='email+yav@ayharano.dev',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Other Audience',
        'Topic :: Other/Nonlisted Topic',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='validator',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    python_requires='>=3.4, <4',

    install_requires=[],

    entry_points={
        'console_scripts': [
            'yav=yav:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/ayharano/yav/issues',
        'Source': 'https://github.com/ayharano/yav/',
    },
)
