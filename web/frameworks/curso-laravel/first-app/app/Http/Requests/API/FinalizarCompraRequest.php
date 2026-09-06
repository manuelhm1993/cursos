<?php

namespace App\Http\Requests\API;

use App\Data\CartProductData;
use App\Rules\ValidarStockProducto;
use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class FinalizarCompraRequest extends FormRequest
{
    private array $productsDTO = [];

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

    public function passedValidation()
    {
        foreach($this->products as $product) {
            $this->productsDTO[] = CartProductData::from([
                'id'       => $product['id'],
                'cantidad' => $product['cantidad'],
            ]);
        }
    }

    public function getProductsDTO(): array {
        return $this->productsDTO;
    }
}
