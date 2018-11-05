"""
    airswap_exercise
    airswap_exercise
"""
from setuptools import setup
import ast
import re

_version_re = re.compile(r'__version__\s+=\s+(.*)')

filepath = 'airswap_exercise' + '/__init__.py'
with open(filepath, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'mock',
    'pytest-cov',
    'pytest-env',
    'pytest'
]

# Edit this according to requirements
install_requires = [
    'click==6.3',
    'pytest==2.9.0',
    'requests==2.20.0'
]


setup(
    name='airswap_exercise',
    version=version,
    include_package_data=True,
    # Include additional description here
    description='airswap_exercise: airswap_exercise',
    long_description='airswap_exercise',
    author='Brandon Ng',
    install_requires=install_requires,
    extras_require={'test': tests_require},
    tests_require=tests_require,
    packages=['airswap_exercise', 'airswap_exercise.cli'],
    entry_points='''
        [console_scripts]
        airswap = airswap_exercise.cli.cli:cli
        '''
)
