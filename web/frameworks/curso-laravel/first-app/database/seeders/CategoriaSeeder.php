<?php

namespace Database\Seeders;

use App\Models\Category;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class CategoriaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $categories = [
            ['nombre' => 'Jeans'],
            ['nombre' => 'Buzos'],
            ['nombre' => 'Remeras'],
            ['nombre' => 'Hoddies'],
        ];

        foreach($categories as $category) {
            Category::FirstOrCreate($category);
        }
    }
}
