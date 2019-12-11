#
from setuptools import setup, find_packages
#
setup(
    name="aspect",
    packages=find_packages(),
    # Needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/jorgeromanespino/PyAspect.git',
    author='Jorge Roman Espino',
    author_email='jorgeromanespino@gmail.com',
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1.2',
    # The license can be anything you like
    license='Apache License 2.0',
    description='Aspect Oriented Design Framework',
)