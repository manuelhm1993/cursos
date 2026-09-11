<div class="container">
    <div class="row">
        @foreach ($categories as $category)
            <div class="col-12">
                <h4>{{ $category->nombre }}</h4>
            </div>

            <div class="col-12">
                <div class="row mt-5 mb-5">
                    @foreach ($category->products as $product)
                        <div class="col-12 col-sm-4">
                            <div class="card" style="width: 18rem;">
                                <img src="..." class="card-img-top" alt="...">
                                <div class="card-body">
                                    <h5 class="card-title">{{ $product->nombre }}</h5>
                                    <h6 class="card-title">{{ $category->nombre }}</h6>
                                    <p class="card-text">Categoría que agrupa todo lo referente a {{ $product->nombre }}</p>
                                    <a href="{{ route('products.index', $product->nombre) }}" class="btn btn-primary">Ver más</a>
                                </div>
                            </div>
                        </div>
                    @endforeach
                </div>
            </div>
        @endforeach
    </div>
</div>