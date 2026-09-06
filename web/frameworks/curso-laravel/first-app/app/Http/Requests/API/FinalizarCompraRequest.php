<?php

namespace App\Http\Requests\API;

use App\Rules\ValidarStockProducto;
use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

use App\Utilities\Traits\HasCartProductsDTO;

class FinalizarCompraRequest extends FormRequest
{
    // Inyección de la lógica horizontal
    use HasCartProductsDTO;
    
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'products'            => 'required|array',
            'products.*.id'       => 'required|integer|exists:products,id',
            'products.*.cantidad' => ['required', 'integer', new ValidarStockProducto], // Uso de regla propia

            'nombre'   => 'required|string',
            'apellido' => 'required|string',
            'email'    => 'required|email',
            'telefono' => 'required|string',

            'tipo_envio'    => ['required', Rule::in('Delivery', 'Pick up')],
            'direccion'     => 'required_if:tipo_envio,Delivery|nullable|string',
            'codigo_postal' => 'required_if:tipo_envio,Delivery|nullable|string',
            'pais'          => 'required_if:tipo_envio,Delivery|nullable|string',
            'estado'        => 'required_if:tipo_envio,Delivery|nullable|string',
            'municipio'     => 'required_if:tipo_envio,Delivery|nullable|string',
        ];
    }
}
