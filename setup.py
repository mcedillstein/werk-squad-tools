from setuptools import setup

import os
import glob

def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()

# taking some of Matt's code from vetrr:

def get_scripts():
    """ Grab all the scripts in the bin directory.  """
    scripts = []
    if os.path.isdir('bin'):
        scripts = [fname for fname in glob.glob(os.path.join('bin', '*'))
                   if not os.path.basename(fname).endswith('.rst')]
    return scripts


scripts = get_scripts()

setup(name='werk-squad-tools',
      version='0.1',
      description='Software for calculating SFR and metallicities for CGM Squared galaxies.',
      long_description=readfile('README.md'),
      url='https://github.com/ktchrn/werk-squad-tools',
      author='Joseph Breneman, Steven Bet, Apurva Goel, Mercedes Thompson, Leonardo Zhu, Sam Johnson, Kirill Tchernyshyov',
      author_email="everyone's email goes here",
      packages=['werksquadtools'],
      license=readfile('LICENSE'),
      scripts=scripts,
    )
