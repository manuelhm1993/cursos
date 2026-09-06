<?php

namespace App\Utilities\Classes;

class Common 
{
    public static function getCategories(): array {
        return [
            "Fideos" => [
                "Moñitos",
                "Fideos largos",
                "Cabello de ángel",
            ],
            "Verduras" => [
                "Tomates",
                "Lechuga",
                "Cebolla",
            ],
        ];
    }
}