from setuptools import find_packages, setup

import versioneer

with open(u'requirements.txt', u'r') as f:
    required = f.read().splitlines()

cmd_class = versioneer.get_cmdclass()

setup(name='Menus',
      version=versioneer.get_version(),
      description='Create cli menus with ease',
      url='https://github.com/JMSwag/Menus',
      author='Digital Sapphire',
      author_email='menus@digitalsapphire.io',
      license='MIT',
      packages=find_packages(),
      zip_safe=True,
      install_requires=required,
      cmdclass=cmd_class,
      )
