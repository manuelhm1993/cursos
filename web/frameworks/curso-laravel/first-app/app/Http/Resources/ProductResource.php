<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class ProductResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        // Transforma un modelo a un array y lo devuelve en json
        return [
            'id'       => $this->id,
            'nombre'   => $this->nombre,
            'stock'    => $this->stock,
            'precio'   => $this->precio,
            // Solo se incluye si el controlador cargó la relación con eager loading
            // make = 1:1 o N:1 (belongsTo o hasOne)
            // collection = 1:N o N:M (hasMany o belongsToMany)
            'category' => CategoryResource::make($this->whenLoaded('category')),
        ];
    }
}
