@extends('layouts.admin')

@section('content')
<div class="row">
    <div class="col-md">
        <div class="card">
            <div class="card-header">
                <strong>Editar</strong> Producto
            </div>
            <div class="card-body">
                {{-- Mostrar los errores de validación --}}
                @include('includes.errores')

                <form action="{{ route('admin.products.update', $product->id) }}" method="post" id="edit-form" enctype="multipart/form-data">
                    @csrf
                    @method('PUT')
                    <div class="form-group">
                        <label for="category_id">Categoría</label>
                        <select class="form-control" name="category_id" id="category_id">
                            <option value="">Seleccionar</option>
                            @foreach ($categories as $category)
                                <option {{ ($category->id === $product->category_id) ? 'selected' : '' }} value="{{ $category->id }}">{{ $category->nombre }}</option>
                            @endforeach
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="nombre">Nombre</label>
                        <input class="form-control" id="nombre" type="text" name="nombre" placeholder="Fideos" value="{{ old('nombre', $product->nombre) }}">
                    </div>

                    <div class="form-group">
                        <label for="precio">Precio</label>
                        <input class="form-control" id="precio" type="number" name="precio" min="0" step="1" value="{{ old('precio', $product->precio) }}">
                    </div>

                    <div class="form-group">
                        <label for="stock">Stock</label>
                        <input class="form-control" id="stock" type="number" name="stock" min="0" step="1" value="{{ old('stock', $product->stock) }}">
                    </div>
                </form>
            </div>
            <div class="card-footer">
                <button class="btn btn-sm btn-primary" type="submit" form="edit-form">Actualizar</button>
                <button class="btn btn-sm btn-danger" type="reset" form="edit-form">Limpiar</button>
            </div>
        </div>
    </div>
</div>
@endsection