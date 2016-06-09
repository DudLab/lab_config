import os

from distutils.core import setup

pkg_dir = os.path.dirname(os.path.abspath(
    __file__
))

readme = ""
readme_filename = os.path.join(pkg_dir, "README.rst")
with open(readme_filename, "r") as readme_file:
    readme = readme_file.read()

setup(
    name="lab_config",
    version="0.1.0",
    license="BSD??",
    description="A package of utilities in use in our lab.",
    long_description=readme,
    author="John Kirkham",
    author_email="kirkhamj@janelia.hhmi.org",
    url="https://github.com/DudLab/lab_config",
    packages=["config"],
    package_data={"config": ["*.ui"]},
    classifiers=[]
)
