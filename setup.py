from setuptools import setup, find_packages

setup(
    name="banco_python",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Thalia Danielle",
    author_email="thalia.dani2@gmail.com",
    description="Uma biblioteca para gerenciar contas bancárias",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thaliadani/sistema_bancario_python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)