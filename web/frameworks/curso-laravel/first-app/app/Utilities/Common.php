<?php

namespace App\Utilities;

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