from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="multicarriage",
    author="xyzpw",
    maintainer="xyzpw",
    url="https://github.com/xyzpw/multicarriage",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    description="Allows the ability to rewrite multiple lines via carriage returns.",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        #none
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
