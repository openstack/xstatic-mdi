from setuptools import setup, find_packages

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
long_description = open('README.txt').read()

setup(
    name='XStatic-mdi',
    description="""mdi 1.6.50 (XStatic packaging standard)""",
    long_description=long_description,
    maintainer="Diana Whitten",
    maintainer_email='hurgleburgler@gmail.com',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'wheel'],
    packages=find_packages(),
    include_package_data=True
)
