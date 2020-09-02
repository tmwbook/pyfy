import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyfy",
    version="0.0.1",
    author="Tom White",
    author_email="twhite@wpi.edu",
    description="A python wrapper for the Spotify API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmwbook/pyfy",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    python_requires=">=3.6"
)
