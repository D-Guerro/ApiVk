from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='ApiVk',
    version='1.0',
    author_email='Guerro.dev@mail.ru',
    url='',
    license='Apache 2.0',
    author='Guerro',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)
