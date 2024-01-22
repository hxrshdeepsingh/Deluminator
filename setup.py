# setup.py

from setuptools import setup, find_packages

setup(
    name='Deluminator',
    version='0.1',
    author='Harshdeep Singh',
    author_email='ishu.cxx@gmail.com',
    packages=find_packages(include=['Deluminator', 'Deluminator.*']),
    package_data={'Deluminator': ['engine/source']},
    install_requires=[
        'click',
        'pyinstaller',
        'pyautogui'
    ],
    entry_points={
        'console_scripts': [
            'Deluminator = Deluminator.main:Deluminator',
        ],
    },
)
