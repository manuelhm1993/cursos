@extends('layouts.main')

@section('title', 'Products')

@section('content')
    <h1>HOME</h1>
    
    <h3>CATEGORIES</h3>

    <div class="container">
        <div class="row">
            @foreach ($categories as $category)

                <div class="col-12 col-sm-3">
                    <div class="col-12 col-sm-4">
                        <div class="card" style="width: 18rem;">
                            <img src="..." class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">{{ $category->nombre }}</h5>
                                <h6 class="card-title">{{ $category->products_count }}</h6>
                                <p class="card-text">Categoría que agrupa todo lo referente a {{ $category->nombre }}</p>
                                <a href="{{ route('products.index', $category->nombre) }}" class="btn btn-primary">Ver más</a>
                            </div>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
@endsection