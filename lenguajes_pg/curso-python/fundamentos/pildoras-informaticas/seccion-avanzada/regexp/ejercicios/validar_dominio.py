import re

def validar_dominio(dominios: list[str], pattern: str) -> list[str]:
    lista_dominios = [*filter(lambda e: re.findall(pattern, e), dominios)]

    return lista_dominios

dominios = [
    "https://enlacepropiedades.com", 
    "http://enlacepropiedades.com", 
    "https://mhenriquez.com", 
    "http://mhenriquez.com",
    "ftps://mhenriquez.com",
    "ftp://mhenriquez.com"
]

r"^(https?|ftps?)://[\w]+\.[a-zA-Z]{2,}"

pattern = r"^ftps?"

print(validar_dominio(dominios, pattern))