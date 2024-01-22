# setup.py

from setuptools import setup, find_packages

setup(
    name='Deluminator',
    version='0.1',
    author='Harshdeep Singh',
    author_email='ishu.cxx@gmail.com',
    license='BSD-3-Clause',
    long_description=open('README.md').read(),
    description="This package is a reverse shell generator for Windows systems that uses sockets to establish a connection. It is highly capable of bypassing antivirus software. The package includes a control server and comes with a number of useful features.",
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
