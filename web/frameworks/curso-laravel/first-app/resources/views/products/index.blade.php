@extends('layouts.main')

@section('title', 'Products')

@section('content')
    <h1>PRODUCTS</h1>

    <div class="container">
        <div class="row">
            @foreach ($products as $product)
                <div class="col-12 col-sm-3 mb-4">
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">{{ $product }}</h5>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
@endsection