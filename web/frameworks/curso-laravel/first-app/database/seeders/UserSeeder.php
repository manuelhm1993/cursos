<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $data = [
            'name'     => 'Manuel Henriquez',
            'email'    => 'admin@mhenriquez.com',
            'password' => bcrypt('password'),
        ];

        $user = User::where('email', $data['email'])->get();

        if($user->isEmpty()) {
            User::create($data);
            $this->command->info('El usuario fue creado exitosamente');
        }
        else {
            $this->command->warn('El usuario ya existe en la base de datos');
        }
    }
}
