import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Trumail", # Replace with your own username
    version="0.0.1",
    author="MateeHash",
    author_email="mattiagiornetta@gmail.com",
    description="A package made for test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MateeHash/Trumail-api-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
