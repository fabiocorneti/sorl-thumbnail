from setuptools import setup
from setuptools import find_packages

version = '3.1'

setup(
    name='sorl',
    version=version,
    description="",
    url='http://code.google.com/p/sorl-thumbnail/',
    packages = [
        "sorl",
        "sorl.thumbnail",
        "sorl.thumbnail.templatetags",
        "sorl.thumbnail.tests",
    ],
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
)
