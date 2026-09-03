<div class="container">
    <div class="row">
        @foreach ($categories as $category)
            <div class="col-12 col-sm-4">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ $category->nombre }}</h5>
                        <p class="card-text">Categoría que agrupa todo lo referente a {{ $category->nombre }}</p>
                        <a href="{{ route('products.index', $category->nombre) }}" class="btn btn-primary">Ver más</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
</div>