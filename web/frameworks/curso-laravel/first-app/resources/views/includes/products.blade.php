<div id="products-wrapper" class="container">
    <div class="row">
        @foreach ($products as $product)
            <div class="col-12 col-sm-3 mb-4">
                <div class="card h-100" style="width: 18rem;">
                    <div class="card-body d-flex flex-column justify-content-between">
                        <div>
                            <h5 class="card-title">{{ $product->nombre }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ $product->category->nombre }}</h6>
                            <p class="card-text">Descripción rápida del producto...</p>
                        </div>
                        <a href="{{ route('products.show', $product->id) }}" class="btn btn-primary mt-3">Ver detalle</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>

    <div class="d-flex justify-content-center mt-4">
        {{ $products->links() }}
    </div>
</div>