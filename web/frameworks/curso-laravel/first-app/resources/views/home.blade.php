@extends('layouts.main')

@section('content')
    <h1>HOME</h1>
    <h2>CATEGORÍAS</h2>

    <div class="container">
        <div class="row">
            @foreach ($categories as $category)
                <div class="col-12 col-sm-4">
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">{{ $category }}</h5>
                            <p class="card-text">Categoría que agrupa todo lo referente a {{ $category }}</p>
                            <a href="{{ route('products.show', $category) }}" class="btn btn-primary">Ver más</a>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>

    <h2>PRODUCTOS</h2>

    @include('includes.products')
@endsection