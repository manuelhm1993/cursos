<?php

namespace App\Utilities\Enums;

enum TipoEnvio: string 
{
    case DELIVERY = 'Delivery';
    case PICK_UP  = 'Pick up';
}