<?php

namespace App\Http\Requests\API;

use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;
use Override;

use App\Utilities\Traits\HasCartProductsDTO;

class CarritoControllerRequest extends FormRequest
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
            'products.*.cantidad' => 'required|integer',
        ];
    }
}
