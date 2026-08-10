<?php

class Vehiculo 
{
    private int $ruedas;
    private int $motor;
    private string $color;

    public function __construct() {
        $this->ruedas = 4;
        $this->motor  = 1600;
        $this->color  = "";
    }

    public function arrancar(): string
    {
        return "El vehículo está encendido";
    }
}