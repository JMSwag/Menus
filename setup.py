from setuptools import find_packages, setup

import versioneer

cmd_class = versioneer.get_cmdclass()

setup(name='Menus',
      version=versioneer.get_version(),
      description='Create cli menus with ease',
      url='https://github.com/JMSwag/Menus',
      author='JMSwag',
      author_email='johnymoswag@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=True,
      cmdclass=cmd_class,
      )
