<?php

class Persona 
{
    // Declarar e iniciar variables dentro del constructor php 8+
    public function __construct(
        private string $nombre,
        private int $edad,
        private string $genero,
        private string $nacionalidad
    ) {}

    // ----------------------------- Métodos accesores
    //
    // ----------------------------- Getters
    public function get_nombre(): string {
        return $this->nombre;
    }

    public function get_edad(): int {
        return $this->edad;
    }

    public function get_genero(): string {
        return $this->genero;
    }

    public function get_nacionalidad(): string {
        return $this->nacionalidad;
    }

    // ----------------------------- Setters
    public function set_nombre(string $nombre): void {
        $this->nombre = $nombre;
    }

    public function set_edad(int $edad): void {
        $this->edad = $edad;
    }

    public function set_genero(string $genero): void {
        $this->genero = $genero;
    }

    public function set_nacionalidad(string $nacionalidad): void {
        $this->nacionalidad = $nacionalidad;
    }
}

// Instanciar una clase
$persona = new Persona("Manuel", 33, "Masculino", "Venezolano");

// Acceder a las propiedades
echo "--------- Datos personales ---------
<br>- Nombre:       {$persona->get_nombre()}
<br>- Edad:         {$persona->get_edad()}
<br>- Género:       {$persona->get_genero()}
<br>- Nacionalidad: {$persona->get_nacionalidad()}
";