import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='CRRD',
    version='0.0.2',
    author="radonyl",
    author_email="alex.l.manstein@gmail.com",
    description='China Railway Raido Decoder', long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='railway radio decoder',
    url='https://github.com/radonyl/CRRD',
    python_requires='>=3.5, <4',
    packages=['CRRD'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
