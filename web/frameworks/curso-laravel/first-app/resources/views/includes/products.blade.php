<div class="container">
    <div class="row">
        @foreach ($products as $product)
            <div class="col-12 col-sm-3 mb-4">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ $product->nombre }}</h5>
                        <h6 class="card-title">{{ $product->category->nombre }}</h6>

                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="{{ route('products.show', $product->id) }}" class="btn btn-primary">Ver detalle</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
</div>