"""
Package definition for pomodoro.
"""
from setuptools import setup


setup(
    name='super-simple-pomodoro',
    version='0.0.1',
    description='A super simple pomodoro timer.',
    author='pushittoprod',
    author_email='pushittoprod@gmail.com',
    python_requires='>=3.7.0',
    package_dir={'': 'src'},
    py_modules=[],
    packages=['pomodoro'],
    entry_points={
        'console_scripts': ['pomodoro=pomodoro:main']
    },
    install_requires=[
        'PyGObject',
        'playsound',
    ],
    extras_require={
        'dev': [
            'pylint',
            'pycodestyle',
        ]
    }
)
