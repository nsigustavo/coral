from setuptools import setup, find_packages
import sys, os

version = '0.1'

with file('README') as readme:
    long_description = readme.read()

setup(name='coral',
      version=version,
      description="Modulo que traduz codigo python para portugues",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='coral linguagem dsl tradutor portugues brasil',
      author='Gustavo Rezende',
      author_email='nsigustavo@gmail.com',
      url='http://nsigustavo.blogspot.com',
      license='',
      package_data = {'coral':['*.yaml']},
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'PyYAML',
          'ipython',
      ],

      entry_points = {
            'console_scripts': [
                'coral = coral.comandos:copilar',
                'coralexec = coral.comandos:executar',
                'icoral = coral.icoral:icoral',
                'traduzir = coral.comandos:traduzir']},
      )
