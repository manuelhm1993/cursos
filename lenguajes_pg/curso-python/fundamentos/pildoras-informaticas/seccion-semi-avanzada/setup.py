""" 
setuptools ya no viene instalado por defecto en python. Se debe instalar: pip install setuptools wheel 
Este método es funcional, pero investigar el pyproject.toml
"""
from setuptools import setup

setup(
    name="paquete_calculos",
    version="1.0.0",
    description="Paquete de redondeo y potencia",
    author="MHenriquez",
    author_email="manuelhm1993@gmail.com",
    url="https://mhenriquez.com",
    packages=["paquetes", "paquetes.calculos"]
)