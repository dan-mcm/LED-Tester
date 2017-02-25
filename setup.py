'''
Created on Feb 24, 2017

@author: Daniel McMahon
'''
from setuptools import setup

setup(name="src",
      version="0.1",
      description="LED Testing for Assignment 3 in COMP30670 2017",
      url="",
      author="Daniel McMahon",
      author_email="daniel.mcmahon2@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['led_tester=src.main:main']
          }
      )