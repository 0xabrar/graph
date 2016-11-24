from setuptools import setup, find_packages

install_requires = [
    "matplotlib",
    "networkx"
    ]

setup_requires = [
    "pytest_runner"
    ]

tests_require = [
    "pytest"
    ]

setup(
    name="Graph",
    version=0.1,

    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,

    author="Abrar Hussain",
    author_email="abrar.a.hussain@gmail.com",
    description="A simple package for learning about graphs in Python.",
    license="PSF",
    keywords="learning graph generate"
)
