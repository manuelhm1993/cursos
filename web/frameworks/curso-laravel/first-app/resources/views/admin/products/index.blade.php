@extends('layouts.admin')

@section('content')
    @include('includes.success')

    <div class="row">
        <div class="col-lg">
            <div class="card">
                <div class="card-header"><i class="fa fa-list"></i> Lista de productos</div>
                <div class="card-body">
                    <table class="table table-responsive-sm">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Precio</th>
                                <th>Stock</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach ($products as $product)
                            <tr>
                                <td>{{ $product->id }}</td>
                                <td>{{ $product->nombre }}</td>
                                <td>{{ $product->precio }}</td>
                                <td>{{ $product->stock }}</td>
                                <td>
                                    <a href="{{ route('admin.products.edit', $product->id) }}" class="btn btn-info">
                                        Editar
                                    </a>
                                    <button type="submit" role="button" class="btn btn-danger" form="borrar-id-{{ $product->id }}" onclick="return confirm('¿Está seguro que desea eliminar este elemento?')">
                                        Borrar
                                    </button>
                                    <form id="borrar-id-{{ $product->id }}" action="{{ route('admin.products.destroy', $product->id) }}" method="post">
                                        @csrf
                                        @method('DELETE')
                                    </form>
                                </td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
@endsection