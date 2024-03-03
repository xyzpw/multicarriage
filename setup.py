from setuptools import setup, find_packages
import multicarriage

def getDesc():
    with open("README.md", 'r') as f:
        return f.read()

setup(
    name="multicarriage",
    author=multicarriage.__author__,
    maintainer=multicarriage.__author__,
    url="https://github.com/xyzpw/multicarriage",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description=multicarriage.__description__,
    version="1.1",
    long_description=getDesc(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    license="MIT",
)
