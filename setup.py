try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='hyunjunkr',
      version='0.1.0',
      packages=['hyunjunkr'],
      package_dir={'hyunjunkr': 'web'},
      install_requires=['Flask'],
      url='http://hyunjun.kr')
