from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto) -> str:
        analisis         = TextBlob(texto)
        tipo_sentimiento = analisis.sentiment.polarity

        if tipo_sentimiento == 0:
            sentimiento = "Neutral"
        elif tipo_sentimiento > 0:
            sentimiento = "Positivo"
        else:
            sentimiento = "Negativo"

        return sentimiento

analizador = AnalizadorDeSentimientos()

resultado = analizador.analizar_sentimiento("This is funny, but it's not interesting for me")

print(resultado)