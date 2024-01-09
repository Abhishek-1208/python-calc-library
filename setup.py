from setuptools import find_packages, setup

setup(
    name="python_temp_library",
    version="0.0.1",
    author="Abhishek Saini",
    author_email="shekabhi1208@gmail.com",
    packages=find_packages(['calculator']),
    description="simple calculator",
    url="https://github.com/Abhishek-1208/python-temp-library",
    install_requires=[],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)