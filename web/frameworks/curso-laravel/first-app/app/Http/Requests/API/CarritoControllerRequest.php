<?php

namespace App\Http\Requests\API;

use App\Data\CartProductData;
use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;
use Override;

class CarritoControllerRequest extends FormRequest
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
            'products.*.cantidad' => 'required|integer',
        ];
    }

    #[Override]
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
