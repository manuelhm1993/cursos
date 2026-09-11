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
            'id'         => $this->id,
            'nombre'     => $this->nombre,
            'stock'      => $this->stock,
            'precio'     => $this->precio,
            'created_at' => $this->created_at,
        ];
    }
}
