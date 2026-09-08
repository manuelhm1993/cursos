<?php

namespace Database\Factories;

use App\Models\Category;
use App\Models\Product;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<Product>
 */
class ProductFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        $category_id = Category::inRandomOrder()->first()->id;

        return [
            'category_id' => $category_id,
            'nombre'      => "Producto ". random_int(1, 9999) ." ". fake()->word(),
            'stock'       => random_int(1, 50),
            'precio'      => fake()->randomFloat(2, 1.0, 10000.0),
            'imagen'      => fake()->imageUrl(),
        ];
    }
}
