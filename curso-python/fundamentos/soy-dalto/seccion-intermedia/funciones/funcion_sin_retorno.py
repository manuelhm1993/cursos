# Creando una función simple
def saludar(lookup, nombre, sexo):
    sexo = sexo.lower()
    adjetivo = ""

    if lookup:
        opciones = {
            "hombre": "titán",
            "mujer": "mi reina"
        }

        # 2. Usamos .get(clave_buscada, valor_por_defecto)
        # Si 'sexo' no es ni "hombre" ni "mujer", asignará "amor" instantáneamente
        adjetivo = opciones.get(sexo, "amor")
    else:
        if sexo == 'mujer':
            adjetivo = "reina"
        elif sexo == 'hombre':
            adjetivo = "titán"
        else:
            adjetivo = "amor"

    print(f"Hola {nombre}, mi {adjetivo} ¿cómo estas?")

# Ejecutar la función
saludar(True, "Sugey", "Mujer")
saludar(False, "Manuel", "Hombre")
saludar(True, "Ender", "No binario")