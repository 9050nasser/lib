from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lib/__init__.py
from lib import __version__ as version

setup(
	name="lib",
	version=version,
	description="First App",
	author="Mohammed Nasser",
	author_email="9050nasser@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
