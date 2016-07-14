from setuptools import setup, find_packages

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page.
long_description = open('README.txt').read()

setup(
    name='XStatic-mdi',
    summary="""mdi 1.4.57 (XStatic packaging standard)""",
    description=long_description,
    maintainer="Diana Whitten",
    maintainer_email='hurgleburgler@gmail.com',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'wheel'],
    packages=find_packages(),
    include_package_data=True
)
