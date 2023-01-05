from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='vinorm_mac',
    version='3.0',    
    description='Python package for text normalization, use for frontend of Text-to-speech Reseach',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/v-nhandt21/Vinorm/tree/vinorm_mac',
    author='Flower_On_Stone',
    author_email='thuanbn03@gmail.com',
    license='AILAB',
    packages=['vinorm_mac'],
    include_package_data=True,
    install_requires=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Free for non-commercial use',
        'Natural Language :: Vietnamese',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)
