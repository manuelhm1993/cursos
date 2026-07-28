import re

class DBController:
    @staticmethod
    def latin_character_validate(parameter: str) -> str:
        response = re.sub(r"[áéíóúÁÉÍÓÚñÑäëïöüÄËÏÖÜ]", "_", parameter)
        response.capitalize()
        
        return response